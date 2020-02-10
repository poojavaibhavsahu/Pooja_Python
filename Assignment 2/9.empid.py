name=input("enter name=")
salary=int(input("enter salary="))
empID=[name,salary]
print("before updating the list=",empID)
empID[0]=input("enter the updated name=")
print("after updating the list=",empID)