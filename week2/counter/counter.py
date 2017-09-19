from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key='thisissecretkey'
@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0
        session['counter'] += 1
    return render_template("index.html")

@app.route('/addtwo', methods=['POST'])
def addtwo():
    print "Two should be added to the counter."
    session['counter'] += 1
    return redirect('/')
@app.route('/reset', methods=['POST'])
def reset():
    print "This is number reset."
    session['counter'] = 0
    return redirect('/')

app.run(debug=True) # run our server
