from flask import Flask, render_template,request

import mysql.connector

db=mysql.connector.connect(host="localhost",user="root",password="root",database="nbs",auth_plugin='mysql_native_password')
cur=db.cursor()

app = Flask(__name__)

@app.route('/')
def homepage():
    cur.execute("select * from schools")
    data=cur.fetchall()
    return render_template("showrecords.html",records=data)

app.run(debug=True)