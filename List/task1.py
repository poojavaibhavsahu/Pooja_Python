name=input('Enter the name')
age=int(input('Enter the age:'))
postalcode=int(input('Enter the postal code:'))
street=input('Enter the street')

PersonDetails=[name,age,postalcode,street]

empId=int(input('Enter the empId'))
salary=input('Enter the salary')
companyName=input('Enter the companyName:')
designation=input('Enter the designation')


JobDetails=[empId,salary,companyName,designation]

PersonDetails.extend(JobDetails)
print(PersonDetails)

print("Size of List",len(PersonDetails))

#EmployeeList=[PersonDetails,JobDetails]

#print(EmployeeList)



