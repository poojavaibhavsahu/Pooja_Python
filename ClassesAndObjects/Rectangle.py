class Employee:
    empId=0
    name=''
    salary=0

    def __init__(self,empId,name,salary):
        self.empId=empId
        self.name=name
        self.salary=salary

    def display(self):
        print(self.empId ," ",self.name," ",self.salary)

e1=Employee(101,"ABC",9000)
e2=Employee(102,"DEF",8000)
e3=Employee(103,"DXG",7000)


if(e1.salary>e2.salary and e1.salary>e3.salary):
    print(e1.name,"has highest salary of",e1.salary)
    e1.display()

elif(e2.salary>e1.salary and e2.salary>e3.salary):
    print(e2.name,"has highest salary of ",e2.salary)
    e2.display()

else:
    print(e3.name,"has highest salary of ",e3.salary)
    e3.display()
