class companey:
    companyName=''
    def __init__(self,companyName):

        self.companyName=companyName

class department(companey):
    dname=''
    def __init__(self,companyName,dname):
        super().__init__(companyName)
        self.dname=dname

class devlopper(department):
    language=''
    def __init__(self,companyName,dname,languages):
        super().__init__(companyName,dname)
        self.language=languages
    def displayDetails(self):
        print(self.companyName,self.dname,self.language)
class tester(department):
    nooftestcases=''
    def __init__(self,companyName,dname,nooftestcases):

        super().__init__(companyName,dname)
        self.nooftestcases=nooftestcases

    def displaydetails(self):
        print(self.companyName,self.dname,self.nooftestcases)
objdevloper=devlopper("infosys","pooja","Java")
objdevloper.displayDetails()
objtester=tester("bmw","iit",123)
objtester.displaydetails()

class managment(department):
    typeofmanagment=''
    def __init__(self,companyName,dname,typeofmanagment):
        super().__init__(companyName,dname)
        self.typeofmanagment=typeofmanagment

class Manager(managment):
    noOfprojects=0

    def __init__(self, companyName, dname, typeofmanagment,noOfprojects):
        super().__init__(companyName, dname,typeofmanagment)
        self.noOfprojects=noOfprojects

    def displayManager(self):
        print(self.companyName," ",self.dname," ",self.typeofmanagment," ",self.noOfprojects)

class hr(managment):
    noofincensitive=0
    def __init__(self,companeyname,dname,typeofmanagment,noofincensitive):
        super().__init__(companeyname,dname,typeofmanagment)
        self.noofincensitive=noofincensitive

    def displayhr(self):
        print(self.noofincensitive,self.companyName," ",self.dname," ",self.typeofmanagment)

objmanager=  Manager("wipro","nit",4,8)
objmanager.displayManager()

objhr=  hr("wipro","nit",4,8)
objhr.displayhr()


