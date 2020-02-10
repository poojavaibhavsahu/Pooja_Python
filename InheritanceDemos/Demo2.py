#Multilevel Inheritance

class Animal:

    def speak(self):
        print("Animal speaking")

class Dog(Animal):
    def bark(self):
        print("Dog barking")

class Cat(Dog):
    def mews(self):
        print("Cat mews")

c=Cat()
c.speak()
c.bark()
c.mews()
