from flask import Flask
from flask_restful import Resource,Api
import pymysql

app=Flask(__name__)
api=Api(app)

class AccountInfoService(Resource):
    def get(self,ano):
        no=int(ano)
        dic={}
        con=pymysql.connect(host='mysql-java-javaee-project.c.aivencloud.com',port=19179,user='avnadmin',password='AVNS_TEZ17S2CIEzgqRcBnb0',database='sharayudb')
        curs=con.cursor()
        curs.execute("select * from accounts where accno=%d" %no)
        data=curs.fetchone()
        if data:
            dic['name']=data[1]
            dic['balance']=data[3]
        else:
            dic['name']='not found'
            dic['balance']=0
        
        con.close()
        return dic

api.add_resource(AccountInfoService,"/acc/search/<ano>")
app.run(debug=True)