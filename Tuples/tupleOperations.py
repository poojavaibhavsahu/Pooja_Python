data1=(1,2,3,4)

data2=('x','y ','z')

data3=data1+data2 #concatenation

print(data3)

print("Length of tuple",len(data1))

#Repetition

tuple1=(1,3,4,['hi']*4)
print(tuple1)

print("To check 1 is present in the tuple",1 in tuple1)#to check 1 is present in the tuple

#Iterating using a loop
for i in tuple1:
    print(i)

# tuple1[0]=99#tuples are immutable
# print(tuple1)

convList=list(tuple1)#converts TUple to List
print(convList)

conTup=tuple(convList)#converts List to tuple
print(conTup)






#tuples are immutable so you cannot modify
tuple1[0]=90
print(tuple1)





# print(data1[0])
# print(data1[0:2])
# print(data2[-3:-1])
# print(data1[0:])
# print(data2[:2])

# data3=data1+data2
# print(data3)
#
# tuple1=(1,2,3,"HELLO")
# tuple2=(4,5,6,"good")
#
#
#
# print(tuple1*2)
# print(tuple1*2)