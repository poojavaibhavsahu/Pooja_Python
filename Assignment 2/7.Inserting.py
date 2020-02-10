size=int(input("enter the size="))
list1=[]
for i in range(1,size+1):
    a=input("enter any text=")
    list1.append(a)
list1.insert(2,"Python is a language")
print(list1)