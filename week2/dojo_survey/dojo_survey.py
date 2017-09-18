from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html", dojo = "Dojo Survey")

@app.route('/results', methods=['POST'])
def create_user():
   
   return render_template("results.html", user= request.form)
app.run(debug=True) 