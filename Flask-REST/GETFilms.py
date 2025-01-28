from flask import Flask,jsonify
from flask_restful import Resource,Api
from pymongo import MongoClient

app=Flask(__name__)
api=Api(app)

class AllCustomers(Resource):
    def get(self,genre):
        client=MongoClient("mongodb+srv://praffull:ethan913@ethancluster.nz1sx.mongodb.net/?retryWrites=true&w=majority&appName=EthanCluster")
        db=client["netflixdb"]
        coll=db["films"]
        dic={'genre':genre}
        lst=list(coll.find(dic))
        lst1=[]
        print(lst)
        for doc in lst:
            doc.pop('_id')
            print(doc)
            lst1.append(doc)
        jsonlist=[doc for doc in lst1]
        return jsonify(jsonlist)

api.add_resource(AllCustomers,'/films/search/<genre>')
app.run(debug=True)
