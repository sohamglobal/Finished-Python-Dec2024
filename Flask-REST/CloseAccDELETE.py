from flask import Flask,request
import pymysql

app=Flask(__name__)

@app.route('/account/close',methods=['DELETE'])
def closeaccount():
    no=int(request.form.get("accno"))
    key=request.form.get("apikey")
    dic={}
    if key=='pm0836':
        
        try:
            con=pymysql.connect(host='mysql-java-javaee-project.c.aivencloud.com',port=19179,user='avnadmin',password='AVNS_TEZ17S2CIEzgqRcBnb0',database='sharayudb')
            curs=con.cursor()
            curs.execute(f"select * from accounts where accno={no}")
            data=curs.fetchone()
            if data:
                curs.execute("delete from accounts where accno=%d" %no)
                con.commit()
                dic['status']='success'
            else:
                dic['status']='not found'
            con.close()
        
        except:
            dic['status']='failed'
    else:
         dic['status']='key error'       
    return dic

app.run(debug=True)
