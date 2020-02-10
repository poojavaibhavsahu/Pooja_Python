#W.A.P TO CHECK WHETHER THE NO. IS ARMSTRONG NO.

x=int(input('Enter a no.'))

sum=0

t=x

while(t!=0):
    sum=sum+(int(t%10))**3
    t=t/10
if(sum==x):
    print('It is an armstrong no.')
else:
    print('It is not an armstrong no.')