from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():

    return render_template ("newtemp.html")

@app.route('/team')
def team1():

    return render_template("team.html")
    
@app.route('/Michael')
def Michael1():
    return render_template("employees.html",name="Michael",data="afhkjahsfjkhsfjhjkashdhas")

@app.route('/Shafeeq')
def Shafeeq1():
    return render_template("employees.html",name="Shafeeq",data="asdfgsgsdfsgsdhujoiuuouidgioljshjlsdjjldkashdhas")


@app.route('/John')
def John1():
    return render_template("employees.html",name="John",data="n xbvmnzbhhkjhgoii giug weug oiusio gs")

@app.route('/James')
def James1():
    return render_template("employees.html",name="James",data="asfhkjahsfjkhsfjhjkashdhas")


app.run()
