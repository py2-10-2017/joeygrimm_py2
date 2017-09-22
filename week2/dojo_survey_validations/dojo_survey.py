from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
@app.route('/')
def index():
  return render_template("index.html", dojo = "Dojo Survey")

@app.route('/results', methods=['POST'])
def create_user():

    errors = False

    if len(request.form['name']) < 1:
       flash("Your name cannot be empty.")
       errors = True

    if len(request.form['email']) < 1:
       flash("Your email cannot be empty.")
       errors = True

    if len(request.form['comment']) < 1:
      flash("Please leave a comment.")
      errors = True

    if len(request.form['comment']) > 120:
       flash("You've commented too much. Please make it less than 120 characters.")
       errors = True

    if errors:
       return redirect('/')


    return render_template("results.html", user= request.form)

app.run(debug=True)
