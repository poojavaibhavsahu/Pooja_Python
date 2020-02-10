list1=[]

limit=int(input('Enter the size of list'))

for i in range(1,limit+1,1):
    items=input('Enter the items of list:')
    list1.append(items)
for i in list1:
    print(i)

del list1[0]
print(list1)
