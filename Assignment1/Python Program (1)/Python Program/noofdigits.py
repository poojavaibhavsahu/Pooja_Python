num=int(input("Enter the number"))
cnt=0
while num>0:
    temp=num%10
    cnt=cnt+1
    num=num//10
print("number of digits:",cnt)