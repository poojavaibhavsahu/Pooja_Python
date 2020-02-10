#W.A.P TO FIND THE SUM OF DIGITS OF A NUMBER

x=int(input('Enter a no.'))

sum=0

t=x

while(t!=0):
    sum=sum+int(t%10)
    t=t/10

print('Sum of digits of',int(x),'is:',sum)
