import pymysql
myconn=pymysql.connect(host='localhost',user='root',password='root', database="mydatabase")
cur=myconn.cursor()

cur.execute("delete from employee1 where empid=104")

print("success")

myconn.commit()

myconn.close()