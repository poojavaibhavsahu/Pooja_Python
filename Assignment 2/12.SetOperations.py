#TAKING 1ST SET
size=int(input("enter size="))
Names=set()
for i in range(1,size+1):
    n=input("enter Names of Teachers=")
    Names.add(n)
print("list of teachers Names=",Names)
#TAKING 2ND SET
size1=int(input("enter size="))
Student=set()
for j in range(1,size1+1):
    n=input("enter Student names=")
    Student.add(n)
print("list of student names=",Student)
#USING UNION OPERATION
union=Names|Student
print("union=",union)
#USING INTERSECTION OPERATION
intersection=Names&Student
print("intersection=",intersection)
#USING DIFFERENCE OPERATION
difference=Names-Student
print("difference=",difference)