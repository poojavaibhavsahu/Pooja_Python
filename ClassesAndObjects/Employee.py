class Employee:

    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary

    def display(self):
        print(self.id," ",self.name," ",self.salary)

e1=Employee(101,"ABC",9000)
e2=Employee(102,"DEF",1000)
e3=Employee(103,"XYZ",2300)

if(e1.salary >e2.salary and e1.salary>e3.salary):
    e1.display()
    #print(e1.name ,"has highest salary of",e1.salary)

elif(e2.salary >e3.salary and e2.salary>e1.salary):

    print(e2.name, "has highest salary of", e2.salary)
    
else:
    print(e3.name, "has highest salary of", e3.salary)

