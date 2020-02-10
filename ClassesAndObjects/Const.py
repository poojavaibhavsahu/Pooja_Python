class Person:

    name=""
    age=0
    def __init__(self,name,age):#Parametized Constructor
        self.name=name
        self.age=age

    def display(self):
        print(self.name," ",self.age)

    def myname(self):
        print(self.name)

p=Person("ABC",9)
p.display()
p.myname("LLL")