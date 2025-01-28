#pip install flask_restful
from flask import Flask
from flask_restful import Resource,Api

app=Flask(__name__)
api=Api(app)

class Soham(Resource):
    def get(self):
        dic={
            "brand":"dell",
            "model":"latitude 5400",
            "processor":"i5 8th gen",
            "ram":"8gb",
            "ssd":"512gb",
            "screen":"14 inch",
            "os":"windows 11 pro",
            "price":89000.00
        }
        return dic

api.add_resource(Soham,"/product")
app.run(debug=True)

'''
use this URL to call the REST API
http://127.0.0.1:5000/product
'''