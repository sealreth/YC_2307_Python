from flask import Flask
from flask_cors import CORS
import felix
import tom

# URL: 
# Python: http://127.0.0.1:5000/
# MainGithub: https://github.com/sealreth/YC_2307_Webshop/pulls
# HTML: file:///C:/Users/Tom%20Nijland/Desktop/YoungCap/TraineeShip/Project/PythonProject/Python.html


app = Flask(__name__)
CORS(app)
@app.route("/")
def hello_world():
    return "<p>Hello, World!!!</p>"

@app.route("/tom")
def tomfunc():
    return tom.mijnfunctie3()

@app.route("/tom/<Age>")
def tomfunc2(Age):
    return tom.mijnfunctie4(Age)





""" @app.route("/felix")
def felixfunc():
    return felix.mijnfunctie() """

""" @app.route("/tweedeendpoint")
def hello_world1():
    return "Iets heel anders teruggeven"

@app.route("/derde/<onsgegeven>")
def hello_world3(onsgegeven):
    return "Dit is ons gegeven"+onsgegeven """