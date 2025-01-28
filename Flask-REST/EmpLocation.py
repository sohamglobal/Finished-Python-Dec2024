from flask import Flask
from flask_restful import Resource,Api
import pymysql

app=Flask(__name__)
api=Api(app)

class EmpLocationInfo(Resource):
    def get(self,loc):
        lst=[]
        
        con=pymysql.connect(host='mysql-java-javaee-project.c.aivencloud.com',port=19179,user='avnadmin',password='AVNS_TEZ17S2CIEzgqRcBnb0',database='sharayudb')
        curs=con.cursor()
        curs.execute("select * from employees where location='%s'" %loc)
        data=curs.fetchall()
        for rec in data:
            dic={}
            dic['name']=rec[1]
            dic['department']=rec[2]
            dic['post']=rec[3]
            dic['salary']=rec[5]
            print(dic)
            lst.append(dic)
        
        return lst

api.add_resource(EmpLocationInfo,"/emp/location/<loc>")
app.run(debug=True)