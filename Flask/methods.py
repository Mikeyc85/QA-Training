from flask import Flask, render_template

app = Flask(__name__)

@app.route('/record')
def forHomepage1():
    return "someone requested for method - get"

@app.route('/record', methods=['POST'])
def forHomepage2():
    return "someone requested for method - post"

@app.route('/record', methods=['DELETE'])
def forHomepage3():
    return "someone requested for method - DELETE"

@app.route('/employees', methods=['GET','POST'])
def forHomepage4():
    return "someone requested for method - get or post"

@app.route('/employees', methods=['PUT'])
def forHomepage41():
    return "someone requested for method - put"

app.run (debug=True)