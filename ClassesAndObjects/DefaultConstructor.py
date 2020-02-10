class Student:

    #Parameterized constructor
    def __init__(myself,rollno,marks):
        myself.rollno=rollno
        myself.marks=marks

    def display(myself):
        print(myself.rollno," ",myself.marks)

obj1=Student(10,90)#parameterized constructor
obj1.display()


