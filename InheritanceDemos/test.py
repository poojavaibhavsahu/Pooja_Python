class School:
    schoolName=''
    def inputSchool(self):
        self.schoolName=input('Enter the schoolName:')

class College:
    clgName=''
    def inputCollege(self):
        self.clgName=input('Enter the colgName:')

class Student(School,College):
    rollno=0
    marks=0
    def inputStudent(self):
        self.rollno=int(input('Enter the rollno:'))
        self.marks=int(input('Enter the marks:'))
    def display(self):
        print(self.rollno," ",self.marks," ",self.schoolName," ",self.clgName)

s=Student()
s.inputStudent()
s.inputCollege()
s.inputSchool()
s.display()
