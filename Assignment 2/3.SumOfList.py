size=int(input("enter size="))
lst=[]
sum=0
for i in range(1,size+1):
    a=int(input("enter a="))
    lst.append(a)
    sum+=a
print("lst=",lst)
print("sum=",sum)