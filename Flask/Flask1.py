from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return "hello my friends"

@app.route('/abc')
def one():
    return "Welcome to Nationwide"


app.run()