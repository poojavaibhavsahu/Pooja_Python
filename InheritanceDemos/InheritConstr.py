class Person:
    def __init__(self,id,name):
        self.id=id
        self.name=name

    def details(self):
        print(self.id,self.name)

class Student(Person):

    def __init__(self,id,name,average):

        #super(). __init__(id,name)
        super(Student,self). __init__(id,name)
        self.average = average

    def details(self):
        print(super().details())
        print(self.average)

obj=Student(101,'ABC',90)
obj.details()




