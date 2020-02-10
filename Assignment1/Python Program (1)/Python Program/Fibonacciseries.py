r=int(input("Enter the range of the fibonacci series:"))
a=0
b=1
print("Fibonacci series")
for i in range(0,r):
    print(a,end=" ")
    sum=a+b
    a=b
    b=sum
