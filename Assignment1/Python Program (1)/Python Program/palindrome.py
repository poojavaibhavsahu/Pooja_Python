num=int(input("Enter the number:"))
n=num
rev=0
while(num>0):
    rem=num%10
    rev=(rev*10)+rem
    num=num//10

if rev==n:
    print(n,"is a palindrome number")
else:
    print(n,"is not a palindrome number")
