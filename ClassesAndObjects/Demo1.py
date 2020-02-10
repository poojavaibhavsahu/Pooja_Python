class AreaCalculator:

    def areaSquare(self,side):
        return side*side

    def areaRectangle(self,length,breadth):
        return length*breadth

    def areaCircle(self,radius):
        return 3.14*radius*radius

side=int(input('Enter the side:'))
length=int(input('Enter the length'))
breadth=int(input('Enter the breadth:'))
radius=float(input('Enter the radius:'))

obj=AreaCalculator()
print("Area of square:",obj.areaSquare(side))
print("Area of rect:",obj.areaRectangle(length,breadth))
print("Area of circle:",obj.areaCircle(radius))


