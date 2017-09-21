from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime
app = Flask(__name__)
app.secret_key='thisissecretkey'

@app.route('/')
def index():

    if 'gold' not in session:
        session['gold'] = 0
        session['activity'] = []
    elif 'gold' in session:
        pass
    print session['gold']
    return render_template("index.html")


@app.route('/process_money', methods =['POST'])
def makingmoney():
    newgold = 0
    time = datetime.now().strftime("%Y/%m/%d %I:%M:%S %p")
    building = request.form['building']

    if request.form['building'] == 'farm':
        newgold = random.randint(10, 20)
        session['gold'] += newgold
        session['activity'].append("You entered the {} and earned {} gold pieces. You have a total of {} gold pieces. {}".format(building, newgold, session['gold'], time))

    elif request.form['building'] == 'cave':
        newgold = random.randint(5, 10)
        session['gold'] += newgold
        session['activity'].append("You entered the {} and earned {} gold pieces. You have a total of {} gold pieces. {}".format(building, newgold, session['gold'], time))

    elif request.form['building'] == 'house':
        newgold = random.randint(2, 5)
        session['gold'] += newgold
        session['activity'].append("You entered the {} and earned {} gold pieces. You have a total of {} gold pieces. {}".format(building, newgold, session['gold'], time))

    elif request.form['building'] == 'casino':
        newgold = random.randint(-50, 50)
        session['gold'] += newgold
        session['activity'].append("You entered the {} and earned {} gold pieces. You have a total of {} gold pieces. {}".format(building, newgold, session['gold'], time))

    print "Added ", newgold," to my gold. I now have...", session['gold']
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():

    if request.form['reset']:
        session['gold'] = 0
        session['activity'] = []
    return redirect('/')

app.run(debug=True)
