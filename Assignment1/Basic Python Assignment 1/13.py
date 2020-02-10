#W.A.P TO PRINT PATTERNS USING NESTED FOR

t=65
for i in range(0,4,1):
    for j in range(0,i+1,1):
        ch=chr(t)
        print(ch,end='')
        t = t + 1
    print()


t=0
n=0
for i in range(0,5,1):
    t=n
    for j in range(0,i+1,1):
        print(t,end='')
    t=t+1

    print()

t =0

for i in range(0, 5, 1):
    t = 1
    for j in range(0, i+1, 1):
        print(t, end='')
        t=t+1



    print()





