#CREATES LIST
size=int(input("enter size="))
colors=[]
for i in range(1,size+1):
    c=input("enter colors=")
    colors.append(c)
print(colors)
size1=int(input("enter size="))
#CREATES TUPLES
Languages=[]
for i in range(1,size1+1):
    L=input("enter Programming Languages=")
    Languages.append(L)
t=tuple(Languages)
print(t)
#CREATES SET
size2=int(input("enter size="))
Numbers=set()
for i in range(1,size2+1):
    n=int(input("enter Numbers="))
    Numbers.add(n)
print(Numbers)
#CREATES DICTIONARY USING VALUES OF LIST TUPLES SET
dict1={"List":colors,"Tuples":t,"Set":Numbers}
print(dict1)




