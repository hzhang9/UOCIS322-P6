# Streaming Service

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class listAllJson(Resource):
    def get(self):
        return None

class listOpenJson(Resource):
    def get(self):
        return None

class listCloseJson(Resource):
    def get(self):
        return None

class listAllCsv(Resource):
    def get(self):
        return None

class listOpenCsv(Resource):
    def get(self):
        return None

class listCloseCsv(Resource):
    def get(self):
        return None

# Create routes
# Another way, without decorators
api.add_resource(listAllJson, '/listAll', '/listAll/json')
api.add_resource(listOpenJson, '/listOpenOnly', '/listOpenOnly/json')
api.add_resource(listCloseJson, '/listCloseOnly', '/listCloseOnly/json')
api.add_resource(listAllCsv, '/listAll/csv')
api.add_resource(listOpenCsv, '/listOpenOnly/csv')
api.add_resource(listCloseCsv, '/listCloseOnly/csv')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
