from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def nonninja():
    return render_template('index.html')

@app.route('/ninja/<color>')
def turtles(color):
    ninjas = {
        'blue':'leonardo',
        'purple':'donatello',
        'red':'raphael',
        'orange':'michelangelo'
    }
    if color in ninjas:
        character = ninjas[color]
    else:
        character = 'notapril'
    return render_template('tmnt.html', character = character)

app.run(debug=True)
