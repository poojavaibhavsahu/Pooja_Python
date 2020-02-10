size=int(input("enter size="))
numbers=[]
for i in range(1,size+1):
    a=int(input("enter a="))
    numbers.append(a)
    count=numbers.count(4)
print(numbers)
print("numbers of 4s in list=",count)
