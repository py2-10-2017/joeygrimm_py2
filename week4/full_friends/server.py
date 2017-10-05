from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
mysql = MySQLConnector(app,'full_friends')

@app.route('/')
def index():
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    return render_template('index.html', friends=friends)

@app.route('/friends', methods=['POST'])
def create():

    if EMAIL_REGEX.match(request.form['email']):
        query = "INSERT INTO friends(first_name, last_name, email, created_at, updated_at) VALUES(:first_name, :last_name, :email, NOW(), NOW())"
        data = {'first_name': request.form['first_name'], 'last_name': request.form['last_name'], 'email': request.form['email']}
        flash("You added a friend.")
        mysql.query_db(query,data)
        return redirect('/')
    else:
        flash("You entered an invalid email address.")

    return redirect('/')

@app.route('/friends/<id>/edit', methods=['GET'])
def edit(id):
    query = "SELECT * FROM friends WHERE id = :id"
    friend = mysql.query_db(query,{'id': id}) [0]
    return render_template('edit.html', friend=friend)

@app.route('/friends/<id>', methods=['POST'])
def update(id):
    if EMAIL_REGEX.match(request.form['updated_email']):
        query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, email = :email, updated_at = NOW() WHERE id = :id"
        data = {'first_name': request.form['updated_first_name'], 'last_name': request.form['updated_last_name'], 'email': request.form['updated_email'], 'id': id}
        mysql.query_db(query,data)
        return redirect('/')
    else:
        flash("You entered an invalid email address editing, try again.")
    return redirect('/')

@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
    query = "DELETE FROM friends WHERE id = :id"
    data = {'id': id}
    flash("You deleted a friend.")
    mysql.query_db(query,data)
    return redirect('/')
    

app.run(debug=True)