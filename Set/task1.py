
size=int(input('How many elements do you want to store in set?'))

myset=set()

sum=0
for i in range(1,size+1):
    num=int(input('Enter positive integers only'))
    myset.add(num)


for i in myset:
    print(i)
    sum=sum+i



print("Sum is:",sum)