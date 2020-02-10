class Student:
    def __init__(self):
        self.rollno=int(input('Enter rollno'))
        self.name=input('Enter the name')
        self.marks=input('Enter the marks')

    def showData(self):
        print(self.rollno," ",self.name," ",self.marks)

#create three objects
s1=Student()
s1.showData()

s2=Student()
s2.showData()

s3=Student()
s3.showData()
