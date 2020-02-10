size=int(input("enter size="))
dict1={}
for i in range(1,size+1):
    subjects = input("enter subjects=")
    marks = int(input("enter marks="))
    dict1[subjects]=marks
print(dict1)
for subjects,marks  in dict1.items():
    print(subjects,"=",marks)
