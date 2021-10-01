from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def forhomepage():
    return render_template("timeshomepage.html")

@app.route('/timestable/<no>')
def fortimestable(no):

    return render_template ("timestable.html",T=int(no))

app.run()
