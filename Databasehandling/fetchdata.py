import pymysql
myconn=pymysql.connect(host='localhost',user='root',password='root', database="mydatabase")
cur=myconn.cursor()
cur.execute("select * from employee1")
#feching the rows fro the cursor object
result=cur.fetchall()
#printing the result
for x in result:
    print(x)
myconn.close()