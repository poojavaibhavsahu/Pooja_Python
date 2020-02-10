import pymysql
myconn=pymysql.connect(host='localhost',user='root',password='root', database="mydatabase")
cur=myconn.cursor()
sql="insert into employee1(name,empid,salary)values('pooja',102,3000)"
var1='vaihbav'
var2=101
var3=3500
cur.execute(sql)
limit=int(input("enter the limit"))


for i in range(1,limit,1):
    name=input("enter the name")
    empid=int(input("enter the empid"))
    salary=int(input("enter the salary"))
    cur.execute("""INSERT INTO employee1 (name,empid,salary) VALUES (%s,%s,%s) """,(var1,var2,var3))
    myconn.commit()
print("successfully insetted")
myconn.close()
