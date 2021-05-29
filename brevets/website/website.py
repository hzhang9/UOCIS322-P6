import flask
from flask import Flask, render_template, request
import requests
import os
import logging

ADDR= os.environ['BACKEND_ADDR']
PORT= os.environ['BACKEND_PORT']
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')


@app.route('/listAJ',methods=['POST'])
def listAJ():
    top=request.form['top']
    if top==None or top.isdigit()==False:
        r = requests.get('http://{}:{}/listAll/json'.format(ADDR,PORT))
    else:
        r = requests.get('http://{}:{}/listAll/json?top={}'.format(ADDR,PORT,top))
    return r.text

@app.route('/listOJ',methods=['POST'] )
def listOJ():
    top=request.form['top']
    if top==None or top.isdigit()==False:
        r = requests.get('http://{}:{}/listOpenOnly/json'.format(ADDR,PORT))
    else:
        r = requests.get('http://{}:{}/listOpenOnly/json?top={}'.format(ADDR,PORT,top))
    return r.text

@app.route('/listCJ',methods=['POST'])
def listCJ():
    top=request.form['top']
    if top==None or top.isdigit()==False:
        r = requests.get('http://{}:{}/listCloseOnly/json'.format(ADDR,PORT))
    else:
        r = requests.get('http://{}:{}/listCloseOnly/json?top={}'.format(ADDR,PORT,top))
    return r.text

@app.route('/listAC',methods=['POST'])
def listAC():
    top=request.form['top']
    if top==None or top.isdigit()==False:
        r = requests.get('http://{}:{}/listAll/csv'.format(ADDR,PORT))
    else:
        r = requests.get('http://{}:{}/listAll/csv?top={}'.format(ADDR,PORT,top))
    return r.text

@app.route('/listOC',methods=['POST'])
def listOC():
    top=request.form['top']
    if top==None or top.isdigit()==False:
        r = requests.get('http://{}:{}/listOpenOnly/csv'.format(ADDR,PORT))
    else:
        r = requests.get('http://{}:{}/listOpenOnly/csv?top={}'.format(ADDR,PORT,top))
    return r.text

@app.route('/listCC',methods=['POST'])
def listCC():
    top=request.form['top']
    if top==None or top.isdigit()==False:
        r = requests.get('http://{}:{}/listCloseOnly/csv'.format(ADDR,PORT))
    else:
        r = requests.get('http://{}:{}/listCloseOnly/csv?top={}'.format(ADDR,PORT,top))
    return r.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
