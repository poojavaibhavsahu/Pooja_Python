list1=[101,"ABC",201.99,11,900,"APPLE","Mango"]
print(list1)

#operation in List
print("Length of a list",len(list1))#starts with 1

list2=["Car","Bike","Cycle",10000,67.00]
#concat or merge two list
mergeList=list1+list2
print(mergeList)

#Repetition

list3=[1,2,3,['Bye']*3,[200]*4]
print(list3)

#PRINT THE the list using for loop

for i in list3:
    print(i,end=",")