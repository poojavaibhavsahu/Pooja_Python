limit=int(input('Enter the size:'))

list1=[]

for i in range(1,limit+1):
    n=int(input("Enter the value:"))
    list1.append(n)
    if(n in list1):
        print(n)



