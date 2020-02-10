size=int(input("enter the size="))
list1=[]
for i in range(1,size+1):
    a=input("enter any text=")
    list1.append(a)
c=input("what do you want to check=")
print(list1)
print("The data",c,"that you want to check in the list is",c in list1)

