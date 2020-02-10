class A:
    def add(self,a,b):
        return a+b

class B(A):
    def add(self,a,b):
       return a-b

obj=B()
print("Sum of two numbers",obj.add(3,3))
print("Sum of three numbers:",obj.add(3,2,))
