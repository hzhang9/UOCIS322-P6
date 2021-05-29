from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')

@app.route('/listAJ')
def listAJ():
    r = requests.get('http://restapi:5000/listAll')
    return r.text
@app.route('/listOJ')
def listOJ():
    r = requests.get('http://restapi:5000/listAll')
    return r.text
@app.route('/listCJ')
def listCJ():
    r = requests.get('http://restapi:5000/listAll')
    return r.text
@app.route('/listAC')
def listAC():
    r = requests.get('http://restapi:5000/listAll')
    return r.text
@app.route('/listOC')
def listOC():
    r = requests.get('http://restapi:5000/listAll')
    return r.text
@app.route('/listCC')
def listCC():
    r = requests.get('http://restapi:5000/listAll')
    return r.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
