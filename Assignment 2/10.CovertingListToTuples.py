size=int(input("enter the size="))
Languages=[]
for i in range(1,size+1):
    s=input("enter languages=")
    Languages.append(s)
print("list=",Languages)
print("list is converted to tuple=",tuple(Languages))
print("tuple is converted to list=",list(Languages))