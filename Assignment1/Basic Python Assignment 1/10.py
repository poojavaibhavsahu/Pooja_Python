#W.A.P TO INPUT STUDENT MARKS BY CONDITION

x=0
tot=0
sub=int(input('Enter the number of subjects:'))


while(x!=sub):

    x = x + 1

    y = int(input('Enter marks:'))

    tot=y+tot

avg=tot/x

print('Your average total of marks is:',avg)

if(avg>=75):
    print('You have achieved DISTINCTION!')
elif(avg>=50):
    print('You have achieved 1ST CLASS!')
else:
    print('You have FAILED!!')

