import pymysql
myconn=pymysql.connect(host='localhost',user='root',password='root', database="mydatabase")
cur=myconn.cursor()


sql="insert into employee1(name,empid,salary)values(%s,%s,%s)"
val=[("john",102,25000),
     ("david",104,45000),
     ("nick",105,50000)]
cur.executemany(sql,val)
print(cur.rowcount,"record inserted!")
myconn.commit()
myconn.close()