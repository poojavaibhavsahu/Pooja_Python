class Person:

    age=0
    name=''
    def __init__(self,age,name):
        self.age=age
        self.name=name

    def display(self):
        print(self.age," ",self.name)

p1=Person(11,"ABC")
p1.display()

p2=Person(12,"pooja")
p2.display()





