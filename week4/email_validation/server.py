from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
mysql = MySQLConnector(app,'email_validation_erd')

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
         if EMAIL_REGEX.match(request.form['email']):
            query = "INSERT INTO emails (email, created_at) VALUES (:email, NOW())"
            data = {'email': request.form['email']}
            mysql.query_db(query, data)
            return redirect('/results')

         else:
            flash("You entered an invalid email address.")
                                            
    return render_template('index.html') 

@app.route('/results', methods =['GET'])
def results():
    query = "SELECT * FROM emails"
    emails =  mysql.query_db(query)
    
    return render_template('results.html', emails=emails)

app.run(debug=True)

