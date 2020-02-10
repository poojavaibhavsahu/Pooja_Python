class Student:

    def __init__(self):
        self.name=input('Enter name')
        self.age=int(input('Enter age'))

    def display(self):
        print(self.name,self.age)

s=Student()
s.display()
