#W.A.P TO CHECK WHETHER THE YEAR IS LEAP YEAR OR NOT

year=int(input('Enter the year no.:'))

if(year%4==0):
    print(year,'is a leap year')
else:
    print(year,'is not a leap year')