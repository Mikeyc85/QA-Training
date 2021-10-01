from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def forHomepage():

    return render_template ("Homepage.html",day=7)

app.run()
