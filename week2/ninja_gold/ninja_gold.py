from flask import Flask, render_template, request, redirect, session
import random, datetime
app = Flask(__name__)
app.secret_key='thisissecretkey'

@app.route('/')
def index():

    if 'gold' not in session:
        session['gold'] = 0

    elif 'gold' in session:
        pass
    print session['gold']
    return render_template("index.html")


@app.route('/process_money', methods =['POST'])
def makingmoney():
    newgold = 0

    if request.form['building'] is 'farm':
        newgold = random.randint(10, 20)
        session['gold'] += newgold

    elif request.form['building'] is 'cave':
        newgold = random.randint(5, 10)
        session['gold'] += newgold

    elif request.form['building'] is 'house':
        newgold = random.randint(2, 5)
        session['gold'] += newgold

    elif request.form['building'] is 'casino':
        newgold = random.randint(-50, 50)
        session['gold'] += newgold

    print "Added ", newgold," to my gold. I now have...", session['gold']
    return redirect('/')

app.run(debug=True)
