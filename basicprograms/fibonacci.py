n=int(input('Enter the number'))
f1=0
f2=1
print(f1,",",f2)

while(n>0):
    f3=f1+f2
    f1=f2
    f2=f3
    print(f3)

