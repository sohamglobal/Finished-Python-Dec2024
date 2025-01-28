from flask import Flask,request
import pymysql

app=Flask(__name__)

@app.route('/account/transfer',methods=['PUT'])
def transfermoney():
    fno=int(request.form.get("fromacc"))
    tno=int(request.form.get("toacc"))
    amt=float(request.form.get("amount"))
    dic={}
    try:
        con=pymysql.connect(host='mysql-java-javaee-project.c.aivencloud.com',port=19179,user='avnadmin',password='AVNS_TEZ17S2CIEzgqRcBnb0',database='sharayudb')
        curs=con.cursor()
        curs.execute("update accounts set balance=balance-%.2f where accno=%d" %(amt,fno))
        con.commit()
        curs.execute("update accounts set balance=balance+%.2f where accno=%d" %(amt,tno))
        con.commit()
        con.close()
        dic['status']='success'
    except:
        dic['status']='failed'
    return dic

app.run(debug=True)
