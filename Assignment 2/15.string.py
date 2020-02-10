size=int(input("enter size="))
str=""
list1=[]
#TRAVERSE USING LOOPS
for i in range(1,size+1):
    s=input("enter string=")
    list1.append(s)
s1=str.join(list1)
print(s1)
#CHECKING THE LENGTH OF STRING
print("length of string=",len(s1))
#CONVERTING THE STRING TO UPPERCASE
print("string is converted to uppercase=",s1.upper())
#CAPITALIZING THE STRING
print("string is capitalized=",s1.capitalize())






