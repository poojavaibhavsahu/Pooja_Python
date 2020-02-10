#Write lamda inside another# function

def add(a,b):
    sum=a+b
    print("Sum is",sum)
    sub=lambda x,y:x-y
    print("Sub is:",sub(9,2))
add(2,4)