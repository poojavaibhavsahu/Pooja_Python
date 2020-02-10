mydict1={101:'ABC',102:'DEF'}
print(mydict1)

mydict2={105:'XYZ',104:'DEF'}
print(mydict2)

mydict1.update(mydict2)#To merge data in dictionary
print(mydict1)








copyDict=mydict2.copy()#to copy data in dictionary
print(copyDict)

list1=[1,2,3,4]
tuple1=("ABC","DEF",9.8)

dict1={101:list1,102:tuple1}
print(dict1)



#print("To get the particular value in dictionary",mydict1.get(104))



