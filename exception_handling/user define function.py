class marksoutofvalue(Exception):
    pass



class student:
    def validmarks(self,marks):
        if(marks>100):
            raise marksoutofvalue()

obj=student()
try:
    obj.validmarks(90)
except marksoutofvalue:
    print("invalid marks")
else:
    print('valid marks')