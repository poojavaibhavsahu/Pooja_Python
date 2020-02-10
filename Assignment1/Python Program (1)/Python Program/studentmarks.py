marks=int(input("Enter the marks of the student:"))
if marks>=0 and marks<50:
    print("Student is Failed")
elif marks>=50 and marks<75:
    print("Student has got 1st class")
elif marks>=75 and marks<=100:
    print("Student has got distinction")
else:
    print("Invalid marks")

