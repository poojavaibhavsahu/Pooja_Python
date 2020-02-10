from abc import ABC,abstractmethod
class A(ABC):#makes a class abstract
    @abstractmethod
    def msg(self):
        pass

    def display(self):#non abstarct method
        print("Hello display method")


class B(A):
    def msg(self):
        print("Hello msg called")

obj=B()
obj.msg()
obj.display()




















# from abc import ABC,abstractmethod
#
# class A(ABC):
#     @abstractmethod
#     def msg(self): #abstract method
#         pass
#
#
# class B(A):
#    def msg(self):
#        print("hi")
#
# obj=B()
# obj.msg()
