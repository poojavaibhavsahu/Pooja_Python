marks=int(input("enter the marks"))
if(marks>0 and marks<50):
    print("student is failed")
elif(marks>50 and marks<75):
    print("student is first class")
elif(marks>75 and marks<100):
    print("student get distinction")
else:
    print("not valid marks")
