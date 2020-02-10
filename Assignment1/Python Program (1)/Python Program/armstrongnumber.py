num=int(input("Enter the number:"))
n=num
sum=0
while (num>0):
    temp=num%10
    sum=sum+(temp*temp*temp)
    num=num//10
print("sum of digits:",sum)
if sum==n:
    print(n,"is a armstrong number")
else:
    print(n,"is not a armstrong number")

