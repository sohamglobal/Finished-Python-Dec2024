from pymongo import MongoClient

class WorkerServices:
    def addnewworker(self,dic):
        try:
            client=MongoClient("mongodb+srv://praffull:mongodb913@ethancluster.nz1sx.mongodb.net/?retryWrites=true&w=majority&appName=EthanCluster")
            db=client["spiderdb"]
            coll=db["workers"]
            coll.insert_one(dic)
            client.close()
            stat="worker added successfully"
        except:
            stat="add worker process failed"
        return stat

