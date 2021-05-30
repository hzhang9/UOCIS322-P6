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
    app.logger.debug(r.content)
    result="ACP Brevet Times (json):\n"
    c_c=0
    for i in r.text:
        if str(i)!='[' and str(i)!=']' and str(i)!='{' and str(i)!='}':
            if c_c==4 and str(i)==",":
                c_c=0
                continue
            else:
                result+=str(i)
        if i==",":
            c_c+=1
    result=result.replace('\n','<br/>')
    return result

@app.route('/listOJ',methods=['POST'] )
def listOJ():
    top=request.form['top']
    if top==None or top.isdigit()==False:
        r = requests.get('http://{}:{}/listOpenOnly/json'.format(ADDR,PORT))
    else:
        r = requests.get('http://{}:{}/listOpenOnly/json?top={}'.format(ADDR,PORT,top))
    app.logger.debug(r.content)
    result="ACP Brevet Open Times (json):\n"
    c_c=0
    for i in r.text:
        if str(i)!='[' and str(i)!=']' and str(i)!='{' and str(i)!='}':
            if c_c==3 and str(i)==",":
                c_c=0
                continue
            else:
                result+=str(i)
        if i==",":
            c_c+=1
    result=result.replace('\n','<br/>')
    return result

@app.route('/listCJ',methods=['POST'])
def listCJ():
    top=request.form['top']
    if top==None or top.isdigit()==False:
        r = requests.get('http://{}:{}/listCloseOnly/json'.format(ADDR,PORT))
    else:
        r = requests.get('http://{}:{}/listCloseOnly/json?top={}'.format(ADDR,PORT,top))
    app.logger.debug(r.content)
    result="ACP Brevet Close Times (json):\n"
    c_c=0
    for i in r.text:
        if str(i)!='[' and str(i)!=']' and str(i)!='{' and str(i)!='}':
            if c_c==3 and str(i)==",":
                c_c=0
                continue
            else:
                result+=str(i)
        if i==",":
            c_c+=1
    result=result.replace('\n','<br/>')
    return result

@app.route('/listAC',methods=['POST'])
def listAC():
    top=request.form['top']
    if top==None or top.isdigit()==False:
        r = requests.get('http://{}:{}/listAll/csv'.format(ADDR,PORT))
    else:
        r = requests.get('http://{}:{}/listAll/csv?top={}'.format(ADDR,PORT,top))
    result="ACP Brevet Times (csv):\n"
    counter=0
    for i in r.text:
        if str(i)!='[' and str(i)!=']' and str(i)!='{' and str(i)!='}' and str(i)!='"':
            if str(i)==',' and counter==4:
                counter=0
                continue
            else:
                result+=str(i)
            if str(i)==",":
                counter+=1
    result=result.replace('\n','<br/>')
    return result


@app.route('/listOC',methods=['POST'])
def listOC():
    top=request.form['top']
    if top==None or top.isdigit()==False:
        r = requests.get('http://{}:{}/listOpenOnly/csv'.format(ADDR,PORT))
    else:
        r = requests.get('http://{}:{}/listOpenOnly/csv?top={}'.format(ADDR,PORT,top))
    result="ACP Brevet Open Times (csv):\n"
    counter=0
    for i in r.text:
        if str(i)!='[' and str(i)!=']' and str(i)!='{' and str(i)!='}' and str(i)!='"':
            if str(i)==',' and counter==3:
                counter=0
                continue
            else:
                result+=str(i)
            if str(i)==",":
                counter+=1
    result=result.replace('\n','<br/>')
    return result

@app.route('/listCC',methods=['POST'])
def listCC():
    top=request.form['top']
    if top==None or top.isdigit()==False:
        r = requests.get('http://{}:{}/listCloseOnly/csv'.format(ADDR,PORT))
    else:
        r = requests.get('http://{}:{}/listCloseOnly/csv?top={}'.format(ADDR,PORT,top))
    result="ACP Brevet Close Times (csv):\n"
    counter=0
    for i in r.text:
        if str(i)!='[' and str(i)!=']' and str(i)!='{' and str(i)!='}' and str(i)!='"':
            if str(i)==',' and counter==3:
                counter=0
                continue
            else:
                result+=str(i)
            if str(i)==",":
                counter+=1
    result=result.replace('\n','<br/>')
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
