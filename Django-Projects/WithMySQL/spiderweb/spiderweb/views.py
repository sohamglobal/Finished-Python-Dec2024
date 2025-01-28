from django.shortcuts import render
from .services import FilmOperations
#import pymysql

# for URL http://127.0.0.1:8000/
def home(request):
    return render(request,"index.html",{'developer':'Sharayu','company':'Spider Projects One'})

def newfilm(request):
    return render(request,"NewFilm.html")

def addfilm(request):
    if request.method=="POST":
        try:
            nm=request.POST.get("filmname")
            yr=int(request.POST.get("relyear"))
            gn=request.POST.get("genre")
            ln=request.POST.get("language")
            rt=float(request.POST.get("imdbrating"))
            #print(f"{nm} {yr} {gn} {ln} {rt}")

            obj=FilmOperations()
            mess=obj.addnewfilmtodb(nm,yr,gn,ln,rt)
            print(mess)
        except:
            print('error in data')
    return render(request,"FilmAdded.html")

def filmreport(request):
    obj=FilmOperations()
    data=obj.retrieveallfilmsdata()
    return render(request,"FilmsReport.html",{"filmsdata":data})

def genresearch(request):
    if request.method=="POST":
        gen=request.POST.get("genre")
        obj=FilmOperations()
        dic=obj.searchfilmsongenre(gen)
    return render(request,"SearchGenreResult.html",dic)

def langsearch(request):
    return render(request,"LanguageSearch.html")

def searchonlang(request,lang):
    obj=FilmOperations()
    dic=obj.findfilmsonlang(lang)
    return render(request,"ShowFilmsOnLanguage.html",dic)

def linkgenresearch(request):
    return render(request,"LinksForGenreSearch.html")

def login(request):
    if request.method=="POST":
        id=request.POST.get("userid")
        ps=request.POST.get("password")
        obj=FilmOperations()
        stat=obj.authenticate(id,ps)

        if stat=="success":
            request.session["userid"]=id
            page="FilmsAdmin.html"
        else:
            page="Failure.html"

    return render(request,page,{"user":id})        

def delete(request):
    return render(request,"DeleteFilm.html")

def delfilm(request):
    if request.method=="POST":
        fid=int(request.POST.get("filmId"))
        obj=FilmOperations()
        status=obj.deletefilm(fid)
    
    uid=request.session.get("userid","unknown")
    return render(request,"Deleted.html",{"status":status,"userid":uid})


def ajaxgenresearch(request):
    return render(request,'ajaxgenresearch.html')

def ajaxgen(request,gen):
    obj=FilmOperations()
    dic=obj.searchfilmsongenre(gen)
    return render(request,"SearchGenreResult.html",dic)
