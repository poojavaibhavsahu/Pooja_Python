class Student:

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

class Marks(Student):

    def __init__(self,name,rollno,marks):
        super.__init__(name,rollno)
        self.marks=marks

class Sports(Marks):

    def __init__(self,name,rollno,marks,score):
        super.__init__(name,rollno,marks)
        self.score=score

    def display(self):
        print(self.name," ",self.rollno," ",self.marks," ",self.score)


s=Sports('ABC',12,90,2)
s.display()
