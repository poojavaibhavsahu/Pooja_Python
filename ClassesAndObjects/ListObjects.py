class Employee:

    def __init__(self,empid,name,salary):
        self.empid=empid
        self.name=name
        self.salary=salary

    def display(self):
        print(self.empid," ",self.name," ",self.salary)


empList=[]

n=int(input('How many objects do you want?+9:'))

for i in range(1,n+1,1):

    empId=int(input('Enter empId:'))
    name=input('Enter name')
    salary=int(input('Enter salary'))

    e=Employee(empId,name,salary)

    empList.append(e)

    e.display()


