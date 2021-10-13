from flask import Flask, render_template,request,redirect
import mysql.connector

db=mysql.connector.connect(host="localhost",user="root",password="root",database="employees",auth_plugin='mysql_native_password')
cursor=db.cursor()


app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("Login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/employee")
def employee():
    cursor.execute("select * from personalInfo")
    data=cursor.fetchall()
    return render_template("Homepage.html",records=data)

@app.route("/personalInfo_entry")
def personalinfo_entry():
    return render_template("personalinfoform.html")

@app.route("/personalInfo_save",methods=["POST"])
def personalinfo_save():

    cursor.execute("select max(empno) from personalInfo")
    newempno=cursor.fetchone()
    name=request.form["name"]
    department=request.form["department"]
    address=request.form["address"]
    country=request.form["country"]
    insertcommand="insert into personalInfo values({0},'{1}','{2}','{3}','{4}')".format((newempno[0]+1),name,department,address,country,)
    cursor.execute(insertcommand)
    db.commit()
    return redirect("/")

@app.route("/deleteemployee/<eno>")
def deleteemployee(eno):
    cursor.execute("delete from personalInfo where empno="+eno)
    db.commit()
    return redirect("/")

@app.route("/editemployee/<empno>")
def editemployee(empno):
    cursor.execute("select * from personalInfo where empno="+empno)
    data=cursor.fetchone()
    return render_template("personalinfoedit.html",record=data)

@app.route("/personalInfo_edit",methods=["POST"])
def personalinfo_edit():

    updatecommand="update personalInfo set empname='{0}',address='{1}' where empno={2}".format(request.form["name"],request.form["address"],request.form["empno"])
    cursor.execute(updatecommand)
    db.commit()
    return redirect("/")

@app.route("/countryvizlist/<country>")
def countryvizlist(country):
    cursor.execute("select * from personalInfo where country='{0}'".format(country))
    listofemployees=cursor.fetchall()

    cursor.execute("select count(*) from personalInfo where country='{0}'".format(country))
    numberofemployees=cursor.fetchone()
    msg="List of Employees from "+country
    return render_template("SpecificList.html",records=listofemployees,number=numberofemployees[0],message=msg)

@app.route("/departmentlist/<dept>")
def deptlist(dept):
    cursor.execute("select * from personalInfo where department='{0}'".format(dept))
    listofemployees=cursor.fetchall()

    cursor.execute("select count(*) from personalInfo where department='{0}'".format(dept))
    numberofemployees=cursor.fetchone()
    msg="List of Employees working in "+dept
    return render_template("SpecificList.html",records=listofemployees,number=numberofemployees[0],message=msg)


app.run(debug=True)