class A:
    def methodA(self):
        print("A called")

class B:
    def methodB(self):
        print("B called")

class C(A,B):
    def methodC(self):
        print("C called")

cobj=C()
cobj.methodA()
cobj.methodB()
cobj.methodC()