print("-----pattern1----")
for i in range(1,5,1):
    for j in range(1,5,1):
        print("*",end=" ")
    print()



print("-----pattern2----")
k=1
for i in range(1,4,1):
    for j in range(1,4,1):
        print(k,end=" ")
        k=k+1
    print()
print("-----pattern3----")
for i in range(1,5,1):
    for j in range(1,i+1,1):
        print("*",end=" ")
    print()

print("-----pattern4----")
k=1
for i in range(1,5,1):
    for j in range(1,i+1,1):
        print(k,end=" ")
        k=k+1
    print()

print("-----pattern5----")

k=65
for i in range(1,4,1):
    for j in range(1,i+1,1):
        ch=chr(k)#converts to character
        print(ch,end=" ")
        k=k+1
    print()


