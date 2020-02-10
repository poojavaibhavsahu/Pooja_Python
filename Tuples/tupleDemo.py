tuple1=()

list1=[]
print(type(tuple1))
print(type(list1))

num=1,2,3,4,5
print(type(num))# by default python takes tuple as a sequence

tuple2=(1,2.9,"Hello",67)
print(tuple2)

#accessing of index and slicing is same as List
print(tuple2[0])
print(tuple2[0:2])
print(tuple2[0:])
print(tuple2[:])

print(tuple2[-1])
print(tuple2[0:-2])

