class Person():
    name=''
    age=''

    def __init__(self,name,age):
        self.name=name
        self.age=age

class Student(Person):
    rollno=0
    marks=0


    def __init__(self,name,age,rollno,marks):
        super().__init__(name,age)
        self.rollno=rollno
        self.marks=marks



    def displayStudent(self):
        print(self.name,"" ,self.age," ",self.rollno, " ", self.marks)

class Employee(Person):

    empId=0
    salary=0

    def  __init__(self,name,age,empId,salary):
        super().__init__(name,age)
        self.empId=empId
        self.salary=salary

    def displayEmployee(self):
        print(self.name,"" ,self.age," ",self.empId, " ", self.salary)

print("*******Student Details**********")
m=Student("ABC",12,1001,90)

m.displayStudent()
print("*******Employee Details*********")
e=Employee("AFRGG",21,100122,90000)

e.displayEmployee()




