import pymysql
myconn=pymysql.connect(host='localhost',user='root',password='root', database="mydatabase")
cur=myconn.cursor()
cur.execute("select * from employee1 where salary=2500")
#feching the rows fro the cursor object
result=cur.fetchone()
#printing the result
for x in result:
    print(x)
myconn.close()