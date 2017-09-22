from flask import Flask, render_template, request, redirect, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
@app.route('/')
def registration():

    return render_template('index.html')

@app.route('/results', methods=['POST'])
def result():
    errors = False

    if len(request.form['firstname']) < 1:
        flash("Your first name is blank. Please enter your name.")
        errors = True

    elif not request.form['firstname'].isalpha():
        flash("Your first name contains a number(s) or special characters.")
        errors = True

    if len(request.form['lastname']) < 1:
        flash("Your last name is blank. Please enter your name.")
        errors = True

    elif not request.form['lastname'].isalpha():
        flash("Your last name contains a number(s) or special characters.")
        errors = True

    if len(request.form['password']) < 8:
        flash("Your password is less than eight characters.")
        errors = True

    if len(request.form['confirmpassword']) < 8:
        flash("Your password is less than eight characters.")
        errors = True

    elif request.form['confirmpassword'] != request.form['password']:
        flash("This password doesn't match the entered password.")
        errors = True

    if len(request.form['email']) < 1:
        flash("Please fill out the email address.")
        errors = True

    elif not EMAIL_REGEX.match(request.form['email']):
        flash("You entered an invalid email address.")

    if errors:
        return redirect('/')

    return render_template('results.html')

app.run(debug=True)
