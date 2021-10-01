from flask import Flask, render_template, request,make_response

app = Flask(__name__)

@app.route('/one')
def cookiesend():
    res=make_response()
    res.set_cookie("color","blue")
    return res

@app.route('/two')
def cookiesreceive():
    c=request.cookies.get("color")
    return "color you chose was: "+c

@app.route('/three')
def cookiesend2():
    res2=make_response()
    res2.set_cookie("name","Michael")
    return res2

@app.route('/four')
def cookiesreceive2():
    n=request.cookies.get("name")
    return "the name you entered  was: "+n

app.run (debug=True)