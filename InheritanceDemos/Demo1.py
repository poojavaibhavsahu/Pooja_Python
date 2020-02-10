#
class School:
    schoolName=''
    def inputSchool(self):
        self.schoolName=input('Enter the schoolname')


class College:
    clgName=''
    def inputColg(self):
        self.clgName=input('Enter the clgName')

class Student(School,College):
    rollno=0
    name=''
    def inpuStudent(self):
        self.rollno=int(input('Enter the rollno'))
        self.name=input('Enter the name')
    def display(self):
        print(self.name," ",self.rollno," ",self.schoolName," ",self.clgName)


s=Student()
s.inpuStudent()
s.inputColg()
s.inputSchool()
s.display()



class school():
    schoolname=" "
    def inputschool(self):
        self.schoolname=input("enter the schoolname")
class  collage():
    clgname=''

