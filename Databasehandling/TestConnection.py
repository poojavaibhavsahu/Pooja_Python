import pymysql
myconn=pymysql.connect(user="root",passwd="root",host="localhost")
print(myconn)