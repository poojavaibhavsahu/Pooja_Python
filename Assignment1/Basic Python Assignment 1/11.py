#W.A.P TO GENERATE FIBONACCI SERIES OF GIVEN RANGE

lim=int(input('Enter the limit of the series:'))

a=0
b=1
c=0
print(b,end=' ')
while(c<lim):
    c=a+b
    a=b
    b=c

    print(c,end=' ')