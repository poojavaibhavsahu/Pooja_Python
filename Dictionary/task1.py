Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}


print("printing Employee data .... ")
print(Employee)

print("Enter the details of the new employee....")

age=int(input(" Enter Age: "))
Employee["Age"] =age

Employee["salary"] = int(input("Enter Salary: "))

print("printing the new data")
print(Employee)