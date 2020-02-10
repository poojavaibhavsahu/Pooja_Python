from abc import ABC,abstractmethod

import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def peri(self):
        pass

class Circle(Shape):
    radius=0
    def __init__(self):
        self.radius=int(input('Enter the radius:'))
        print(math.pi)

    def area(self):
        return math.pi*self.radius*self.radius

    def peri(self):
        return 2*math.pi*self.radius


class Rectangle(Shape):
    length=0
    breadth=0

    def __init__(self):
        self.length=int(input('Enter the length:'))
        self.breadth=int(input('Enter the breadth:'))

    def area(self):
        return self.length*self.breadth

    def peri(self):
        return 2*(self.length+self.breadth)


c=Circle()
print("Area of circle:",round(c.area()))
print("Peri of circle:",c.peri())

r=Rectangle()
print("Area of rect:",r.area())
print("Peri of rect:",r.peri())