from first import Bhav
from flask import Flask
from flask_restful import Api,Resource,reqparse

#creating rest apis
app = Flask(__name__)
api = Api(app)
   
   #rest api to get all the stocks whose name starts from the given value
   # example http://127.0.0.1:5000/stock/VEDA
class IndividualStocks(Resource):

    def __init__(self):
        self.x = Bhav()

    def get(self,name):
        self.x.downloadExtract()
        self.x.readCSV()
        self.x.storeInRedis()
        return self.x.printValues(name) , 200
    
    def post(self,name):
        pass
    
    def put(self,name):
        pass
    
    def delete(self,name):
        pass

#display all the stocks 
class allStocks(Resource):
    def __init__(self):
        self.x = Bhav()

    def get(self):
        self.x.downloadExtract()
        self.x.readCSV()
        self.x.storeInRedis()
        return self.x.printValues() , 200
    
    def post(self,name):
        pass
    
    def put(self,name):
        pass
    
    def delete(self,name):
        pass


api.add_resource(IndividualStocks,"/stock/<string:name>")
api.add_resource(allStocks,"/stock/")
app.run(debug=True)
