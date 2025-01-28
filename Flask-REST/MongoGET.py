from flask import Flask,jsonify
from flask_restful import Resource,Api
from pymongo import MongoClient

app=Flask(__name__)
api=Api(app)

class AllCustomers(Resource):
    def get(self):
        client=MongoClient("mongodb+srv://praffull:mongodb913@ethancluster.nz1sx.mongodb.net/?retryWrites=true&w=majority&appName=EthanCluster")
        db=client["spiderdb"]
        coll=db["customers"]
        lst=list(coll.find())
        lst1=[]
        print(lst)
        for doc in lst:
            doc.pop('_id')
            print(doc)
            lst1.append(doc)
        jsonlist=[doc for doc in lst1]
        return jsonify(jsonlist)

api.add_resource(AllCustomers,'/customers/all')
app.run(debug=True)
