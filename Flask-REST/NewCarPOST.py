from flask import Flask,request
import pymysql

app=Flask(__name__)

@app.route('/car/add',methods=['POST'])
def newcar():
    cid=request.form.get('carid')
    nm=request.form.get('modelnm')
    co=request.form.get('company')
    pr=float(request.form.get('price'))
    dic={}
    try:
        con=pymysql.connect(host='mysql-java-javaee-project.c.aivencloud.com',port=19179,user='avnadmin',password='AVNS_TEZ17S2CIEzgqRcBnb0',database='sharayudb')
        curs=con.cursor()
        curs.execute("insert into cars values('%s','%s','%s',%.2f)" %(cid,nm,co,pr))
        con.commit()
        con.close()
        dic['status']='success'
    except:
        dic['status']='failed'
    
    return dic

app.run(debug=True)

