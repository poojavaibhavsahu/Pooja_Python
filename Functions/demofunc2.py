pi=3.14
def area(radius):
    return pi*radius*radius

def circum(radius):
    return 2*pi*radius

def diameter(radius):
    return 2*radius


radius=float(input('Enter the radius'))
print("Area is:",area(radius))
print("Circum is:",circum(radius))
print("Diameter is:",diameter(radius))

