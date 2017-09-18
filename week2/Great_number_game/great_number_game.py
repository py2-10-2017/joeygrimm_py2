import random
from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key='thisissecretkey'
@app.route('/')
def index():
    session['number'] = random.randrange(0,101)
    print session['number']
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guess():

    errors = False

    if int(request.form['guess']) < 1:
        flash("You entered a zero. Please pick between 1 and 100.")
        errors = True

    if int(request.form['guess']) is "":
        flash("You didn't enter a number. Please pick between 1 and 100.")
        errors = True


    if int(request.form['guess']) > 100:
        flash("That number is too large. Please pick a number between 1 and 100.")
        errors = True

    if errors == True:
        return redirect ('/')

    if int(request.form['guess']) is session['number']:
        return render_template("correct.html")

    else:
        print session['number']
        return render_template("guess_again.html")
  

app.run(debug=True) 
