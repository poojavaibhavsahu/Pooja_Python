import xlrd
import pymysql
# Open the workbook and define the worksheet
book = xlrd.open_workbook("abc.xlsx")
sheet = book.sheet_by_index(0)
xlRows=sheet.nrows
xlColumns=sheet.ncols
print(sheet.nrows)
print(sheet.ncols)
for i in range(xlRows):
    VEmpid = sheet.cell_value(2, 0)
    Vage = sheet.cell_value(2, 1)
    VSalary = sheet.cell_value(2, 2)
    VDesignation = sheet.cell_value(2, 3)

    print("Vale of emp id -", VEmpid)
    print("Value of Vage-", Vage)
    print("Value of Emp Age -", VSalary)
    print("Value of Emp VDesignation -", VDesignation)

# Establish a MySQL Connection
myconn = pymysql.connect (host="localhost", user="root", passwd="root", db="mydatabase")
# Get the cursor, which is used to traverse the database, line by line
cur = myconn.cursor()
# Create the INSERT INTO sql query
query1 = "INSERT INTO pyemployee(employee_id,age,salary,designation) VALUES (%s, %s, %s,%s)"
# Create a for loop to iterate through each row in the xls file, starting from
query2="select * from pyemployee where employee_id='101'"
for r in range(1, sheet.nrows):

    employee_id = sheet.cell(r,0).value
    Age= sheet.cell(r,1).value
    salary = sheet.cell(r,2).value
    designation=sheet.cell(r,3).value


    # Assign values from each row
    values = (employee_id,Age,salary,designation)
    # Execute sql query
    cur.execute(query1, values)
# Close the cursor
cur.close()
#Commit the transaction
myconn.commit()
#Close the database connection
myconn.close()