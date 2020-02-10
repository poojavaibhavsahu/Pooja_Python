class Fruit:
    def eat(self):
        print("Eating fruit")

class RedApple(Fruit):
    def appleEat(self):
        print("Eating apple")

class GreenApple(Fruit):
    def greenapple(self):
        print("Eating green apple")

r=RedApple()
r.eat()
r.appleEat()

g=GreenApple()
g.eat()
g.greenapple()
