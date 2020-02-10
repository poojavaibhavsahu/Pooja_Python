import pymysql
myconn=pymysql.connect(host='localhost',user='root',password='root', database="mydatabase")
cur=myconn.cursor()
def createtable():
    dbs = cur.execute("create table student (rolno int(10),name varchar(40),marks int(4))")
    print("table created")
#createtable()
def insertrecord():
    # cur.execute("insert into student values(104,'vaibhav',45)" )
    # print("record inserted")
    sql = "insert into student(rolno,name,marks)values(%s,%s,%s)"
    val = [( 11,"john", 90),
           (12,"david", 104),
           (13,"nick", 105, )]
    cur.executemany(sql, val)
    print(cur.rowcount, "record inserted!")
    myconn.commit()

#insertrecord()

def update():
    cur.execute(" update student set name='alex' where rolno=104")
    myconn.commit()
    print("success")
#update()
def delete():
    cur.execute("delete from student where rolno=104")
    myconn.commit()
    print("sucess")
#delete()
def showdata():
    cur.execute("select * from student")
    result = cur.fetchall()

    for i in result:
        print(i)

showdata()

myconn.close()