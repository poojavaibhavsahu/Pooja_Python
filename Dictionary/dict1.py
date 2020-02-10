data={101:'ABC',102:'DEF',102:'XYZ'}
print(data)

Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}
print(type(Employee))
print("printing Employee data .... ")
print(Employee)

print(Employee["Age"])

Employee["Company"]="wipro"
print(Employee)

del Employee['Age']
print(Employee)

