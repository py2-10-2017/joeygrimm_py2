from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', phrase = "Welcome! This is the index.html file for the Landing Page assignment. Please type in localhost:5000/ninja or localhost:5000/dojo for more information.")

@app.route('/ninja')
def ninja():
    return render_template('ninjas.html', ninja_desc = "A ninja or shinobi was a covert mercendary or agent in feudal Japan.", ninja_text = "The functions of the ninja included espionage, sabotage, infiltration, assassination and guerrilla warfare.")

@app.route('/dojo')
def dojo():
    return render_template('dojo.html', dojo ="Please fill out the form below.")

app.run(debug=True)
