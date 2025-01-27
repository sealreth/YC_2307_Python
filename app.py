from flask import Flask
from flask_cors import CORS
import felix
import tom
import group

# URL: 
# Python: http://127.0.0.1:5000/
# MainGithub: https://github.com/sealreth/YC_2307_Webshop/pulls
# HTML: file:///C:/Users/Tom%20Nijland/Desktop/YoungCap/TraineeShip/Project/PythonProject/Python.html
# DATA SOURCE: https://www.kaggle.com/datasets/prajwal6362venom/diwali-sales 

# Flask:
# flask --app app.py --debug run

app = Flask(__name__)

#HTML:
@app.route("/tombarchart2/<kategorie>")
def tomapppy3(kategorie):
    return tom.chartbarfunctie3(kategorie)
@app.route("/JobEarnings")
def baanapp():
    return tom.JobEarnings()
@app.route("/ProdEarnings")
def prodapp():
    return tom.ProdEarnings()
@app.route("/AgeSexAmount")
def agesexdapp():
    return tom.AgeSexAmount()
@app.route("/State")
def stateapp():
    return tom.State()
@app.route("/HeatmapAgeProdID")
def heatapp():
    return tom.HeatmapAgeProdID()

#LowCode, Java, Powerapp(?)
@app.route("/Producten")
def Prods():
    return group.Producten()




#Extra App.Routes:
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
@app.route("/tombarchart")
def tomapppy():
    return tom.chartbarfunctie2()
@app.route("/felixchartbar")
def felixapppy():
    return felix.chartbarfunctie()

@app.route("/felixchartbar2/<kategorie>")
def felixapppy2(kategorie):
    return felix.chartbarfunctie2(kategorie)


app.debug = True
if __name__ == '__main__':
    app.run()
