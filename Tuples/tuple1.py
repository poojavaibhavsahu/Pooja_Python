abc=1,2,3,4  #by default it is taken as tuple
print(type(abc))
print(abc)

tupl1=('a','xyz',10.90)
print(tupl1)

tup=()
print(tup)

mtup=(1,)
print(mtup)

mtup1=(1,2,3,4,"abc")

mtup2=mtup1 # copying of tuples

print(mtup2)

print(mtup2[0])  #print the first element
print(mtup2[-1])   #print the last element

print(mtup2[:])   #print all the elements using slicing

print(mtup2[1:])

print(mtup2[1:3])

print(mtup2[1:-2])

mytuple1=(1,2,3,4,"SWE",2,0)
mytuple2=(23,4343,555,"AWE")

print(mytuple1+mytuple2)#merge two tuples using + operator

mytuple3=(1,2,3,'Hello'*3)

print(mytuple3)



mytuple3[0]=99 # cannot modify as tuples ar immutable

del(tupl1) # can delete the whole  tuple
print(tupl1)

print("Length of tuple:",len(mytuple3))