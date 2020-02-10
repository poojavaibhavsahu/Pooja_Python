#task 3
size=int(input("How many items do you want to enter ?"))
person_details={}


for i in range(1,size+1,1):
    name=input('Enter your name:')
    age=int(input('What is the age'))
    #name is the key and age is value
    person_details[name]=age # storing the input from user for items

for x,y in person_details.items():

    print(x,":",y)