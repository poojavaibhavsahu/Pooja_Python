class Student:

  name=''
  rollno=0

  def __init__(self,name,rollno):
      self.name=name
      self.rollno=rollno

class Marks(Student):
    marks=0

    def __init__(self,name,rollno,marks):
        super().__init__(name,rollno)#inherit construtor from Parent class
        self.marks=marks

    def display(self):
        print(self.name," ",self.marks,self.rollno)

class Sports(Marks):
    score=0
    def __init__(self,name,rollno,marks,score):
        super().__init__(name,rollno,marks)
        self.score=score



name=input('Enter the name')
rollno=int(input('Enter the rollno'))
marks=int(input('Enter the marks:'))
score =int(input('Enter the score'))

m=Sports(name,rollno,marks,score)
m.display()


