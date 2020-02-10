year=int(input("Enter the year in 4 digits:"))
if year%4==0 and year%100!=0:
    print(year,"year is leap year")
elif year%100==0 and year%400==0:
    print(year, "year is leap year")
elif year%400==0:
    print(year, "year is leap year")
else:
    print(year, "year is not a leap year")
