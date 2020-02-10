#creates an empty file

fileobj = open("raja.txt","x")
#
# fileobj.close()

#crate an write a content in a file
# fileobj = open("raja.txt","a")
# fileobj.write("pooja")
# fileobj.close()

# to read a file
# fileobj = open("raja.txt","r")
# content=fileobj.read()
# print(content)
#loop in file
# for i in content:
#     print(i,end="")
fileobj=open("raja.txt","r")
content=fileobj.read()
print(content)
for i in content:
    print(i,end="")
fileobj.close()