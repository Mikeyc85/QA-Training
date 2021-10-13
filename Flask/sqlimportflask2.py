from flask import Flask, render_template,request

import mysql.connector

db=mysql.connector.connect(host="localhost",user="root",password="root",database="nbs",auth_plugin='mysql_native_password')
cursor=db.cursor()

app = Flask(__name__)

@app.route("/")
def homepage():
    cursor.execute("select * from schools")
    data=cursor.fetchall()
    return render_template("showrecords.html",records=data)

@app.route("/input")
def input():
    return render_template("input.html")

@app.route("/processform",methods=["POST"])
def processingForm():
    regno=request.form['regno']
    name=request.form['name']
    marks=request.form['marks']
    query="insert into schools values ({0}, '{1}',{2})".format(regno,name,marks)

    cursor.execute(query)
    db.commit()
    return "record inserted"
    

app.run(debug=True)