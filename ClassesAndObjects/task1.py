class Rectangle:

    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.length*self.breadth

    def peri(self):
        return 2*(self.length+self.breadth)


l=int(input('Enter the length'))
b=int(input('Enter the breadth'))
r=Rectangle(l,b)
print("Area of rect",r.area())
print("Peri of rect",r.peri())
