class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

class Marks(Student):
    def __init__(self,name,rollno,marks):
        #Inherit constructors
        super(). __init__(rollno,name)
        self.marks=marks

    def display(self):
        print(self.name," ",self.rollno," ",self.marks)

m=Marks("ABC",12,90.4)
m.display()