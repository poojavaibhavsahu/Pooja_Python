# 1.Create Account class with a default constructor and take input from user for accName,accNo and balance.
# Write the following functions :
# a)display()—to display details
# b)deposit()---take amount as argument
# c)withdraw()—take amount  as argument—also print a message if the amount is insufficient..
# d)checkBalance()—to display the total amount after deposit and withdraw.
#
#

class account:
   accname=''
   accno=0
   balance=0
   def __init__(self ):
      self.accname=input("enter the accname")
      self.accno=int(input("enter the accno"))
      self.balance=int(input("enter the balance"))

   def display(myself):
         print(myself.accname, " ", myself.accno, "",myself.balance)

   def deposite (self,ammount):
         self.balance=self.balance+ammount
         print("Amoiunt after deposit",self.balance)
   def withdraw(self,ammount):
      if (ammount>self.balance):
         print("ammount is insufficient")
      else:
         self.balance=self.balance-ammount
   def checkbalance(self):
      print("total ammount is",self.balance)







obj1=account()
obj1.display()
obj1.deposite(200)
obj1.checkbalance()
obj1.withdraw(4000)
obj1.balance()