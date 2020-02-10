for i in range(1,4,1):
    for j in range(1,4,1):
        print("*",end=" " )
    print()

k=1
for i in range(1,4,1):
    i=i+1
    for j in range(1,4,1):

        print(k,end=" ")
        k=k+1
    print()


k=1
for i in range(1,4,1):
    for j in range(1,i+1,1):
        print(k,end=" ")
        k=k+1
    print()


for i in range(1,4,1):
    for j in range(1,i+1,1):
        print("*",end=" ")
    print()

a=65
for i in range(1,4,1):
    for j in range(1,i+1,1):
        ch=chr(a)
        print(ch,end=" ")
        a=a+1

    print()

