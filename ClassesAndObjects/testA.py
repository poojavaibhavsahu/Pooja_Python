
class Employee:

    # name=''
    # salary=0

    def insertDetails(self):
        self.empId=int(input('Enter the empid'))
        self.name=input('Enter the name:')
        self.salary=int(input('Enter the salary:'))

    def display(self):
        print(self.empId,"\n ",self.name," ",self.salary)


