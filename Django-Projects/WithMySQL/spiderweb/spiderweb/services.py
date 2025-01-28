import pymysql

class FilmOperations:
    def searchfilmsongenre(self,gen):
        dic={}
        con=pymysql.connect(host='mysql-python-ethan-python.c.aivencloud.com',port=26428,user='avnadmin',password='AVNS_ethan913',database='sharayudb')
        curs=con.cursor()
        curs.execute("select * from films where genre='%s'" %gen)
        data=curs.fetchall()
        dic['searchresult']=data
        con.close()
        return dic
    
    def addnewfilmtodb(self,nm,yr,gn,ln,rt):
        con=pymysql.connect(host='mysql-python-ethan-python.c.aivencloud.com',port=26428,user='avnadmin',password='AVNS_ethan913',database='sharayudb')
        curs=con.cursor()
        curs.execute("insert into films(filmname,relyear,genre,language,imdbrating) values('%s',%d,'%s','%s',%.1f)" %(nm,yr,gn,ln,rt))
        con.commit()
        con.close()
        return 'new film added successfully'
    
    def retrieveallfilmsdata(self):
        con=pymysql.connect(host='mysql-python-ethan-python.c.aivencloud.com',port=26428,user='avnadmin',password='AVNS_ethan913',database='sharayudb')
        curs=con.cursor()
        curs.execute("select * from films")
        data=curs.fetchall()
        #print(data)
        con.close()
        return data

    def findfilmsonlang(self,lang):
        dic={}
        con=pymysql.connect(host='mysql-python-ethan-python.c.aivencloud.com',port=26428,user='avnadmin',password='AVNS_ethan913',database='sharayudb')
        curs=con.cursor()
        curs.execute("select * from films where language='%s'" %lang)
        data=curs.fetchall()
        dic['language']=lang
        dic['searchresult']=data
        con.close()
        return dic

    def deletefilm(self,fid):
        con=pymysql.connect(host='mysql-python-ethan-python.c.aivencloud.com',port=26428,user='avnadmin',password='AVNS_ethan913',database='sharayudb')
        curs=con.cursor()
        cnt=curs.execute("delete from films where filmid=%d" %fid)
        con.commit()
        con.close()
        if cnt==1:
            stat="success"
        else:
            stat="failed"
        return stat

    def authenticate(self,uid,psw):
        stat=None
        con=pymysql.connect(host='mysql-python-ethan-python.c.aivencloud.com',port=26428,user='avnadmin',password='AVNS_ethan913',database='sharayudb')
        curs=con.cursor()
        curs.execute("select * from users where userid='%s' and pswd='%s'" %(uid,psw))
        data=curs.fetchone()
        if data:
            stat="success"
        else:
            stat="failed"
        #print(uid)
        #print(psw)
        #print(stat)
        con.close()
        return stat
