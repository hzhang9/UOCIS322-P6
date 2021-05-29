from flask import Flask,request
from flask_restful import Resource, Api
import pymongo
from pymongo import MongoClient
import os

app = Flask(__name__)
api = Api(app)
client= MongoClient('mongodb://'+os.environ['MONGODB_HOSTNAME'],27017)
db=client.tododb

class listAJ(Resource):
    def get(self):
        top=request.args.get("top")
        result=[]
        items=list(db.tododb.find())
        counter=1
        bre_order={}
        if top==None or len(items)<int(top):
            for item in items:
                result.append({'ACP Brevet Times Instance {}'.format(counter):{'miles':item['miles'],'km':item['km'],'location':item['location'],'open':item['open'],'close':item['close']}})
                counter+=1
            return {'ACP Brevet Times Display':result}
        else:
            for i in range(int(top)):
                result.append({'ACP Brevet Times Instance {}'.format(counter):{'miles':items[i]['miles'],'km':items[i]['km'],'location':items[i]['location'],'open':items[i]['open'],'close':items[i]['close']}})
                counter+=1
            return {'ACP Brevet Times Display':result}

class listOJ(Resource):
    def get(self):
        top=request.args.get("top")
        result=[]
        items=list(db.tododb.find())
        counter=1
        if top==None or len(items)<int(top):
            for item in items:
                result.append({'ACP Brevet Open Times Instance {}'.format(counter) :{'miles':item['miles'],'km':item['km'],'location':item['location'],'open':item['open']}})
                counter+=1
            return {'ACP Brevet Open Times Display':result}
        else:
            for i in range(int(top)):
                result.append({'ACP Brevet Open Times Instance {}'.format(counter):{'miles':items[i]['miles'],'km':items[i]['km'],'location':items[i]['location'],'open':items[i]['open']}})
                counter+=1
            return {'ACP Brevet Open Times Display':result}

class listCJ(Resource):
    def get(self):
        top=request.args.get("top")
        result=[]
        items=list(db.tododb.find())
        counter=1
        if top==None or len(items)<int(top):
            for item in items:
                result.append({'ACP Brevet Open Times Instance {}'.format(counter) :{'miles':item['miles'],'km':item['km'],'location':item['location'],'close':item['close']}})
                counter+=1
            return {'ACP Brevet Close Times Display':result}
        else:
            for i in range(int(top)):
                result.append({'ACP Brevet Open Times Instance {}'.format(counter):{'miles':items[i]['miles'],'km':items[i]['km'],'location':items[i]['location'],'close':items[i]['close']}})
                counter+=1
            return {'ACP Brevet Close Times Display':result}

class listAC(Resource):
    def get(self):
        top=request.args.get("top")
        result=[]
        items=list(db.tododb.find())
        headers='miles,km,location,open,close'
        result.append({"ACP Brevet Times Headers":headers})
        counter=1
        if top==None or len(items)<int(top):
            for item in items:
                values=','.join([item['miles'],item['km'],item['location'],item['open'],item['close']])
                result.append({"ACP Brevet Time Values {}".format(counter):values})
                counter+=1
            return {'ACP Brevet Times Display':result}
        else:
            for i in range(int(top)):
                values=','.join([items[i]['miles'],items[i]['km'],items[i]['location'],items[i]['open'],items[i]['close']])
                result.append({"ACP Brevet Time Values {}".format(counter):values})
                counter+=1
            return {'ACP Brevet Times Display':result}

class listOC(Resource):
    def get(self):
        top=request.args.get("top")
        result=[]
        items=list(db.tododb.find())
        headers='miles,km,location,open'
        result.append({"ACP Brevet Times Headers":headers})
        counter=1
        if top==None or len(items)<int(top):
            for item in items:
                values=','.join([item['miles'],item['km'],item['location'],item['open']])
                result.append({"ACP Brevet Time Values {}".format(counter):values})
                counter+=1
            return {'ACP Brevet Open Times Display':result}
        else:
            for i in range(int(top)):
                values=','.join([items[i]['miles'],items[i]['km'],items[i]['location'],items[i]['open']])
                result.append({"ACP Brevet Time Values {}".format(counter):values})
                counter+=1
            return {'ACP Brevet Open Times Display':result}


class listCC(Resource):
    def get(self):
        top=request.args.get("top")
        result=[]
        items=list(db.tododb.find())
        headers='miles,km,location,close'
        result.append({"ACP Brevet Times Headers":headers})
        counter=1
        if top==None or len(items)<int(top):
            for item in items:
                values=','.join([item['miles'],item['km'],item['location'],item['close']])
                result.append({"ACP Brevet Time Values {}".format(counter):values})
                counter+=1
            return {'ACP Brevet Close Times Display':result}
        else:
            for i in range(int(top)):
                values=','.join([items[i]['miles'],items[i]['km'],items[i]['location'],items[i]['close']])
                result.append({"ACP Brevet Time Values {}".format(counter):values})
                counter+=1
            return {'ACP Brevet Close Times Display':result}


# Create routes
# Another way, without decorators
api.add_resource(listAJ, '/listAll', '/listAll/json')
api.add_resource(listOJ, '/listOpenOnly', '/listOpenOnly/json')
api.add_resource(listCJ, '/listCloseOnly', '/listCloseOnly/json')
api.add_resource(listAC, '/listAll/csv')
api.add_resource(listOC, '/listOpenOnly/csv')
api.add_resource(listCC, '/listCloseOnly/csv')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
