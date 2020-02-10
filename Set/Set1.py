#create a Set
values={1,2,3,"ABC",66,3,40.4}
print(type(values))
print(values)

#add data to set
values.add(101)
print(values)

values.add("XYZ")
print(values)

print("Size of Set",len(values))


values.remove(101)#it gives an error if you enter unknown data
print(values)

values.discard("aaa")#it does not give any error if u enter unknown data
print(values)












# mydetails=set()
# print(type (mydetails))
#
#
# mydetails.add('abc')
# mydetails.add('Pune')
# mydetails.add('abc')
# print(mydetails)
#
#


