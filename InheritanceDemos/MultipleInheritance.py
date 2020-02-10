class School:
    schoolName=''
    def __init__(self,schoolName):
        self.schoolName=schoolName


class College:
    clgName=''
    def __init__(self,clgName):
        self.clgName=clgName

class Student(School,College):
    rollno=0
    name=''

    def __init__(self,schoolName,clgName,rollno,name):

        School.__init__(self,schoolName)
        College.__init__(self,clgName)
        self.rollno=rollno
        self.name=name


    def display(self):
        print(self.rollno," ",self.name," ",self.schoolName," ",self.clgName)

s=Student("ITS","colleg1",101,"ABC")
s.display()



