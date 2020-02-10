
import pymysql
myconn = pymysql.connect(host='localhost',user='root',passwd='root',database='mydatabase')
cur=myconn.cursor()
dbs=cur.execute("create table customer( rollno int(10),name varchar(40),salary int(4))")
print("tbl created successfully")
myconn.close()