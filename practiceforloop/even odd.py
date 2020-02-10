limit=int(input("enter the limit"))
sum=0
for i in range(1,limit+1,1) :
    if(i % 2== 0 ):
        print("even no is",i)
        sum=sum+i
print(sum)



