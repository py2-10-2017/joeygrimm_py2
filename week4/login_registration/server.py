from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'login_registration')

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/register', methods=['POST'])
def create():
    print request.form
    errors = False

    if len(request.form['first_name']) < 2:
        flash("Your first name is blank. Please enter your name.")
        errors = True

    elif not request.form['first_name'].isalpha():
        flash("Your first name contains a number(s) or special characters.")
        errors = True

    if len(request.form['last_name']) < 2:
        flash("Your last name is blank. Please enter your name.")
        errors = True

    elif not request.form['last_name'].isalpha():
        flash("Your last name contains a number(s) or special characters.")
        errors = True

    if len(request.form['password']) < 8:
        flash("Your password is less than eight characters.")
        errors = True

    if request.form['confirmpassword'] != request.form['password']:
        flash("This password doesn't match the entered password.")
        errors = True

    if not EMAIL_REGEX.match(request.form['email']):
        flash("You entered an invalid email address.")
        errors = True

    if errors:
        return redirect('/')

    else:
        
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        pw_hash = bcrypt.generate_password_hash(password)
        insert_query = "INSERT INTO users (first_name, last_name, email, pw_hash, created_at, updated_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW())"
        query_data = {  'first_name': first_name,'last_name': last_name, 'email': email, 'pw_hash': pw_hash }
        mysql.query_db(insert_query, query_data)
        return render_template('user.html')
    
    

@app.route('/login', methods=['POST'])
def login():
    print request.form
    # you can save all your request.form keys to variables to save some typing
    email = request.form['email']
    password = request.form['password']

    # run validations
    if not EMAIL_REGEX.match(email):
        flash('email is not valid')

    if not len(password) > 7:
        flash("password isn't valid")

    if not '_flashes' in session:
        # only query the db if we encountered 0 errors
        try:
            login_query = 'SELECT * FROM users WHERE email = :email'
            login_data = {'email': email}
            user = mysql.query_db(login_query, login_data)
            hashed = user[0]['password']
            # ^ this breaks if user is empty, which means they've typed a bad email
            print "<<< about to test password vs hash >>>", hashed, password
            it_worked = bcrypt.check_password_hash(hashed, password)
            print "login success:", it_worked
        except:
            flash('invalid username or password')
            it_worked = False

        if it_worked:
            session['id'] = user[0]['id']
            return render_template('user.html')

    return redirect('/')


app.run(debug=True)