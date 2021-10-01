from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return """
    
    <html>
    <center> <h1> Welcome to Nationwide </h1><center>
    <a href='http://localhost:5000/team'> Our Leadership Team </a> <br>
    <a href= 'http://localhost:5000/services'> Services </a> <br>
    <a href= 'http://localhost:5000/aboutus'> About Us </a> <br>
    </html>
    """



@app.route('/abc')
def one():
    return "Hello my friends"

@app.route('/aboutus')
def abtus():
    return "We are building society, Nationwide!"

@app.route('/team')
def team1():
    return """
    
    <html>
    
    <center> <h2> Our leadership team: <h2> <center>
    <a href='http://localhost:5000/jogarner'> Jo Garner - Nationwides CEO</a> <br>
    <a href='http://localhost:5000/patrickeldridge'> Patrick Eldridge - Nationwides COO </a> <br>
    <a href= 'http://localhost:5000/'> Return to homepage </a> <br>
    
    </html>
    """

@app.route('/services')
def serv():
    return """
    
    <html>

    <center> <h2> We offer the following services to our members <h2> <center>
    <a href= 'http://localhost:5000/banking'>Banking products </a><br>
    <a href= 'http://localhost:5000/savings'>Savings products </a><br>
    <a href= 'http://localhost:5000/creditcards'>Credit Cards </a><br>
    <a href= 'http://localhost:5000/loans'>Personal Loans </a><br>
    <a href= 'http://localhost:5000/mortgages'>Mortgages </a><br>
    <a href= 'http://localhost:5000/'> Return to homepage </a> <br>

</html>

"""

@app.route('/jogarner')
def jog():
    return "Jo is our CEO ehhfsdhjhjksdfhkjshdf"

@app.route('/patrickeldridge')
def pat():
    return "Patrick is our chief of staff asjhdjlkashfhaf"

@app.route('/banking')
def bank():
    return "the products we offer for banking are dfg  g dgndfg "

@app.route('/savings')
def sav():
    return "the products we offer for savings are fgh dgh dfgh dfgh "

@app.route('/creditcards')
def ccards():
    return "the products we offer for credit cards are  dfg dfgh dfgh dfgh "

@app.route('/loans')
def loan():
    return "the personal loans are fgh dfgh dfgh dfgh df "

@app.route('/mortgages')
def mort():
    return "the products we offer for mortgagess are dfgh dfgh dfgh dfgh dfgh "

app.run()