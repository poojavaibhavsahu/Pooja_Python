class A:
    s1='ABC'
    def funct1(self):
        print("Value is",self.s1)

class B(A):
    s='DEF'
    def fucnt2(self):
        print("Value in child class",self.s)

        print(super().s1)
        super().funct1()


obj=B()
obj.fucnt2()


