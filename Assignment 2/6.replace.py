size=int(input("enter the size="))
list1=[]
list2=[]
for i in range(1,size+1):
    n1=int(input("enter numbers="))
    list1.append(n1)
print(list1)
for j in range(1,size+1):
    n2=int(input("enter numbers="))
    list2.append(n2)
print(list2)
list1.remove(list1[size-1])
list1.append(list2)
print(list1)
