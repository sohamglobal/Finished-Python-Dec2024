from django.shortcuts import render
from .services import WorkerServices
from pymongo import MongoClient

def home(request):
    return render(request,'index.html')

def newworker(request):
    return render(request,'NewWorker.html')

def addworker(request):
    if request.method=="POST":
        try:
            wid=int(request.POST.get("workerId"))
            nm=request.POST.get("name")
            dp=request.POST.get("department")
            po=request.POST.get("post")
            lo=request.POST.get("location")
            sl=float(request.POST.get("salary"))
            dic={}
            dic['workerid']=wid
            dic['name']=nm
            dic['department']=dp
            dic['post']=po
            dic['location']=lo
            dic['salary']=sl
            print(dic)
            obj=WorkerServices()
            stat=obj.addnewworker(dic)

            mess=stat
        except:
            print('error in data')
            mess="error in data"
    
    return render(request,"EmpAdded.html",{'status':mess})
    
def searchworker(request):
    result={}
    if request.method=="POST":
        try:
            wid=int(request.POST.get("workerid"))
            dic={'workerid':wid}
            
            client=MongoClient("mongodb+srv://praffull:ethan913@ethancluster.nz1sx.mongodb.net/?retryWrites=true&w=majority&appName=EthanCluster")
            db=client["spiderdb"]
            coll=db["workers"]
            for doc in coll.find({'workerid':wid}):
                result['name']=doc['name']
        except:
            result['name']='not found'
    
    print(result)
    return render(request,"SearchResult.html",result)
