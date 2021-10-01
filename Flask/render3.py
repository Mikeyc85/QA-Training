from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():

    return render_template ("newtemp.html")

@app.route('/team')
def team1():

    return render_template("team2.html")
    
@app.route('/employee/<na>/<dept>')
def employeeinfo(na,dept):
    d=""
    if dept=="1":
        d="HR Department"
    if dept=="2":
        d="IT Department"
    return render_template("employees2.html",name=na,department=d)
app.run()
