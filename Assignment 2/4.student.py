Student=[]
for i in range(1,11):
    names=input("enter names=")
    Student.append(names)
print(Student)
for j in range(1,11):
    subjects = input("enter subjects=")
    Student.append(subjects)
print("list=",Student)
#removes the element at index 1
Student.remove(Student[1])
print("Elemet at index 1 is removed=",Student)
#removes the last element
Student.remove(Student[-1])
print("Elemet at last index is removed=",Student)
#prints the list in reverse order
Student.reverse()
print("Elements are printed in reverse order=",Student)