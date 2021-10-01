from flask import Flask, render_template, request,make_response,redirect

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route('/login')
def login1():
    return render_template("login.html")

@app.route('/details/<name>')
def details(name):
    if name!="michael":
        return redirect("/login")
    else:
        return render_template("details.html")

app.run (debug=True)