# size=int(input("enter the size"))
#
# studentdata={101:25,102:36,102:45}
# for size in studentdata:
#     print(studentdata)

size=int(input('Enter the size of dictionary'))
Student_Data={}
for i in range(1,size+1,1):
    rollno=int(input('Enter the rollno'))
    mark=int(input('Enter the marks:'))

    Student_Data[rollno]=mark
# print(Student_Data)

for i ,j in Student_Data.items():
    print(i,"---->",j)