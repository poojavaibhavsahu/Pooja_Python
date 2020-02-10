
tup1=(1,2,3,4,4,45)
print("Length of tuple:",len(tup1))

print("Index of tuple:",tup1.index(2))

print("Count the number of times element occured",tup1.count(4))

print("Smallest element:",min(tup1))

print("Largest element:",max(tup1))




#convert a tuple to List

aaa=list(tup1)
print(aaa)

#convert list to tuple
bbb=tuple(aaa)
print(bbb)