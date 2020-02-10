A={1,2,3,4,5,6}
B={2,3,4,9,10}

# print(A.union(B))
# print(A|B)

A.update(B)
print(A)

# A.clear()
# print(A)
#removes the first value
A.pop()
print(A)