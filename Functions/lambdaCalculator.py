num1=int(input('Enter the first number:'))
num2=int(input('Enter the second number:'))

sum=lambda num1,num2:num1+num2
diff=lambda num1,num2:num1-num2
mul=lambda num1,num2:num1*num2
div=lambda num1,num2:num1//num2

print("Sum is:",sum(num1,num2))
print("Difference is:",diff(num1,num2))
print("Multiply is",mul(num1,num2))
print("Division is:",div(num1,num2))


