add = lambda a:a+10
# a is an argument and a+10 is an expression which got evaluated and returned.
print("sum = ",add(20))


num=int(input('Enter a number:'))
square=lambda num:num**2
print("Square of a number:",square(num))



x = lambda a,b:a+b # a and b are the arguments and a+b is the expression which gets evaluated and returned.
print("sum = ",x(20,10))