size=int(input("enteer the limit"))
myset=set()

sum=0
for i in range(1,size+1):
    num=int(input('Enter the value'))
    myset.add(num)
    sum=sum+num
print(myset)
print("Sum of set",sum)