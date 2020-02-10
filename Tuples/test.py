values= 1,2,34,"ABC","XYZ",90.8
print(type(values))#by default any sequence is taken as Tuple

tuple1=(10,90,"ABC","PQR","QWE",9090,90.9,21)
print(tuple1)

#indexing
print(tuple1[0])
print(tuple1[-1])
print(tuple1[-2])

#slicing
print(tuple1[0:2])
print(tuple1[:])
print(tuple1[:-1])
print(tuple1[-3:-1])
