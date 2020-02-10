class Shape:
    def area(self,radius):
        print("NO shape found")


class Circle(Shape):
    def area(self,radius):
        print("Area is",3.14*radius*radius)

c=Circle()
c.area(2)
