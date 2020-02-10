import re
#cheack the string starts with hello
str="hello world"
x= re.findall("^hello",str)
if(x):
    print("yes,the string start with 'hello'" )
else:
    print("no match")
    #cheack the string end of "world"
x=re.findall("world$",str)
if (x):
    print("yes,the string ends with'world'")
else:
    print("no match")