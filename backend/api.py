from flask import Flask, request
from flask_restful import Resource, Api
from predykcja_meczy import predykacja_meczy_wynik
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/prediction/*": {"origins": "*"}})
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'about' : 'Hello World'}
    
    def post(self):
        some_json = request.get_json()
        return {'you sent' : some_json}, 201
    
class Multi(Resource):
    def get(self, num):
        return {'result' : num*10}

class Prediction(Resource):
    def get(self, data):
        data = str(data)
        print(len(data))
        if len(data) == 5:
                data = '0'+data
        print(data)
        a = data[0:2]
        print(a)
        b = data[2:4]
        print(b)
        c = data[4:]
        print(c)
        data = a+'/'+b+'/'+c
        print(data)
        return {'result' : predykacja_meczy_wynik(data)}
        #return(data)
        
    
    
api.add_resource(HelloWorld, '/')
api.add_resource(Multi, '/multi/<int:num>')
api.add_resource(Prediction, '/prediction/<int:data>')

if __name__ == '__main__':
    app.run(debug=False)

