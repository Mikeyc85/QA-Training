from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return "hello my friends"

@app.route('/abc')
def one():
    return "Welcome to Nationwide"

@app.route('/aboutus')
def abtus():
    return "We are building society, Nationwide!"

@app.route('/team')
def team1():
    return """Our leadership team:
    Jo Garner - CEO
    Patrick Eldrige - COO etc
    """

@app.route('/services')
def serv():
    return "We offer banking products, savings products, credit cards, loans and mortgages to our members"

app.run()