name=input('Enter the name:')
rollno=int(input('Enter the rollno'))
marks=float(input('Enter the marks'))

Student=(name,rollno,marks)

print(Student)

for i in Student:
    print(i)




StudentDetails=list(Student)

print(StudentDetails)

StudentDetails[2]=100
print(StudentDetails)