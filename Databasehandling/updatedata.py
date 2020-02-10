import pymysql
myconn=pymysql.connect(host='localhost',user='root',password='root', database="mydatabase")
cur=myconn.cursor()
cur.execute(" update employee1  set name='alex' where empid=103")
myconn.commit()
print("success")


myconn.close()