from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("/input2.html")

@app.route("/processform",methods=["POST"])
def processingform():
    return render_template("data.html",name=request.form["n"],salary=request.form["s"],country=request.form["country"])

app.run (debug=True)