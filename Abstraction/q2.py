 # Create Employee class with a default  constructor  and take input from user for      empId,eName,salary.
# Write a function  to display employee details…
# Create atleast three objects and call the display function respectively.
# Find out the highest salary of an employee….
 #
 #/
class employee:
     empid=0
     ename=' '
     salary=0

     def __init__(self,empid,ename,salary):
         self.empid=empid
         self.ename=ename
         self.salary=salary
     def display(self):
         print(self.empid,self.ename,self.salary)

e1=employee(121,'pooja',23000)
e2=employee(122,'vaibhav', 45000)
e3=employee(123,'ranu',50000)
e1.display()
e2.display()
e3.display()
if (e1.salary > e2.salary and e1.salary > e3.salary):
     e1.display()
     # print(e1.name ,"has highest salary of",e1.salary)

elif (e2.salary > e3.salary and e2.salary > e1.salary):

     print(e2.ename, "has highest salary of", e2.salary)

else:
     print(e3.ename, "has highest salary of", e3.salary)


