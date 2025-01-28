from flask import Flask
from flask_restful import Resource,Api
import pymysql

app=Flask(__name__)
api=Api(app)

class AccountTypeInfo(Resource):
    def get(self,typ):
        lst=[]
        
        con=pymysql.connect(host='mysql-java-javaee-project.c.aivencloud.com',port=19179,user='avnadmin',password='AVNS_TEZ17S2CIEzgqRcBnb0',database='sharayudb')
        curs=con.cursor()
        curs.execute("select * from accounts where acctype='%s'" %typ)
        data=curs.fetchall()
        for rec in data:
            dic={}
            dic['name']=rec[1]
            dic['balance']=rec[3]
            print(dic)
            lst.append(dic)
        
        return lst

api.add_resource(AccountTypeInfo,"/acc/type/<typ>")
app.run(debug=True)