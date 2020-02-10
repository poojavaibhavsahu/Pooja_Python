# limit=int(input("enter the limit"))
# list1=[]
#
# no=int(input('Enter the number'))
#
# for i in range(1,limit+1,1):
#     sum=0
#     sum=sum+no
#     print("sumof value",sum)
#
# for i in list1:
#     print(i)

limit=int(input("enter the limit"))
list1=[]
sum = 0
for i in range(1,limit+1,1):

    no = int(input('Enter the number'))
    list1.append(no)
    sum=sum+no

print(list1)

print("Sum is", sum)


