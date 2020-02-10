#W.A.P TO CHECK WHETHER THE NUMBER IS A PALINDROME OR NOT

num=int(input('Enter the number:'))

y=num

rev=0

while(num>0):
    t=num%10
    rev=(rev*10)+t
    num =int(num/10)
if(y==rev):
    print('It is a palindrome')
else:
    print('It is not a palindrome')
