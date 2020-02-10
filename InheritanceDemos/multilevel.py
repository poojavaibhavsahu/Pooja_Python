class Student():
    name=''
    rollno=''

    def input(self):
        self.name=input('Enter name')
        self.rollno=int(input('Enter rollno'))

class Marks(Student):

    marks=0
    def inputMarks(self):
        self.marks=input('Enter marks')

class Sports(Marks):
    score=0
    def inputScore(self):
        self.score=int(input('Enter score:'))

    def display(self):
        print(self.name," ",self.rollno," ",self.marks," ",self.score)


s=Sports()
s.input()
s.inputMarks()
s.inputScore()
s.display()
