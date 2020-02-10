num1=int(input('Enter first number'))

num2=int(input('Enter second number'))

def add(a,b):

  return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a//b

print("Sum of two numbers",add(num1,num2))
print("Sub of two numbers",sub(num1,num2))
print("Mul of two numbers",mul(num1,num2))
print("Div of two numbers",div(num1,num2))





#default arguments

def printData(name,age=12):
    print("My name is ",name ,"My age is:",age)
printData("ABC")