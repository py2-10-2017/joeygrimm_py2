# import dependencies
from flask import Flask, request, render_template, redirect, session, flash
from mysqlconnection import MySQLConnector
import re
from flask_bcrypt import Bcrypt

# begin app and mysql objects
app = Flask(__name__)
app.secret_key = "ashjewlgblsdgb"
mysql = MySQLConnector(app, 'wall')
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# begin routes
@app.route('/')
def index():
    get_all_query = "SELECT * FROM users"
    users = mysql.query_db(get_all_query)
    return render_template('index.html', users=users)


@app.route('/register', methods=['POST'])
def register():
    # errors saved to a list
    errors = []

    if len(request.form['first_name']) < 2:
        errors.append('first name must be at least 2 characters long')
    elif not request.form['first_name'].isalpha():
        errors.append('first name must contain only letters')

    if len(request.form['last_name']) < 2:
        errors.append('last name must be at least 2 characters long')
    elif not request.form['last_name'].isalpha():
        errors.append('last name must contain only letters')

    if not EMAIL_REGEX.match(request.form['email']):
        errors.append('email must be valid')

    if not len(request.form['password']) >= 8:
        errors.append('password must be at least 8 characters')
    elif not request.form['confirm_password'] == request.form['password']:
        errors.append('password and confirm password must match exactly')

    # Errors flash prior to generating the hashed pw and nothing submitted to the database
    if errors:
        for error in errors:
            flash(error)
        return redirect('/')
    else:
        hashed_pw = bcrypt.generate_password_hash(
            request.form['password']
        )
        user_data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': hashed_pw
        }
        register_query = """INSERT INTO users
        (first_name, last_name, email, hashed_pw, created_at, updated_at)
        VALUES
        (:first_name, :last_name, :email, :password, NOW(), NOW())
        """
        new_user_id = mysql.query_db(register_query, user_data)
        print new_user_id
        if new_user_id is not 0:
            session['id'] = new_user_id
        else:
            flash('user creation failed')
        return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    # you can save all your request.form keys to variables to save some typing
    print request.form
    email = request.form['email']
    password = request.form['password']

    # run validations
    print re.match(EMAIL_REGEX, "joeygrimm86@gmail.com")
    if not re.match(EMAIL_REGEX,email):
        flash('email is not valid')

    if not len(password) > 7:
        flash("password isn't valid")

    if not '_flashes' in session:
        # only query the db if we encountered 0 errors
        try:
            login_query = 'SELECT * FROM users WHERE email = :email'
            login_data = {'email': email}
            user = mysql.query_db(login_query, login_data)[0]
            hashed = user['hashed_pw']
            # ^ this breaks if user is empty, which means they've typed a bad email
            it_worked = bcrypt.check_password_hash(hashed, password)
        except:
            flash('invalid username or password')
            it_worked = False

        if it_worked:
            session['id'] = user['id']
            flash("Welcome {}".format(user['first_name']), category="success")
            return redirect('/dashboard')

    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/dashboard')
def dashboard():
    get_messages_query = "SELECT messages.content, messages.id, first_name, last_name, messages.created_at FROM messages\
                          JOIN users ON messages.id=user_id"
    messages = mysql.query_db(get_messages_query)

    get_comments_query = "SELECT comments.content, message_id, comments.created_at, first_name, last_name FROM comments\
                          JOIN messages ON messages.id=comments.message_id\
                          JOIN users ON users.id=comments.user_id"
    comments = mysql.query_db(get_comments_query)
    print comments
    if 'id' not in session:
        return redirect('/')
    return render_template('dashboard.html', messages=messages, comments=comments)

@app.route('/post_message', methods=['POST'])
def create_message():
    new_message_query = "INSERT INTO messages (user_id, content, created_at, updated_at)\
                         VALUES (:user_id, :content, NOW(), NOW())"
    new_message_data = {
        "user_id": int(session['id']),
        "content": request.form['content']
    }
    mysql.query_db(new_message_query, new_message_data)
    print mysql.query_db(new_message_query, new_message_data)
    return redirect('/dashboard')

@app.route('/post_comment/<message_id>', methods=['POST'])
def create_comment(message_id):
    new_comment_query = "INSERT INTO comments (user_id, message_id, content, created_at, updated_at)\
                         VALUES (:user_id, :message_id, :content, NOW(), NOW())"
    new_comment_data = {
        "user_id": session['id'],
        "message_id": message_id,
        "content": request.form["content"]
    }
    mysql.query_db(new_comment_query, new_comment_data)
    print mysql.query_db(new_comment_query, new_comment_data)
    return redirect('/dashboard')


app.run(debug=True)