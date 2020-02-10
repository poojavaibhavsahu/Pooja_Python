class ageexception(Exception):
    pass


class rollercoster:
    def validage(self):
        age=int(input("enter the age"))
        if (age<12):
            raise ageexception()
        elif (age>65):
            raise ageexception()
        else:
            print("enjoy the rides")


obj=rollercoster()
try:
    obj.validage()

except ageexception:
    print("invalid age")

