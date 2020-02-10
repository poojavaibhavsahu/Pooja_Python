import xlrd
import pymysql


# Open the workbook and define the worksheet
book = xlrd.open_workbook("E:\\Puja_python\\PythonPrograms\\filehandling\\abc.xlsx")
sheet = book.sheet_by_index(0)

xlRows=sheet.nrows
xlColumns=sheet.ncols

myconn=pymysql.connect(host='localhost',user='root',password='root', database="mydatabase")
cur=myconn.cursor()

query = "INSERT INTO pyemployee (employee_id,age,salary,designation,dateofjoining) VALUES (%s,%s,%s,%s,%s)"

# Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
for i in range(xlRows):
	for j in range(xlColumns):
		# employee_id	= sheet.cell(0).value
		# age	= sheet.cell(1,1).value
		# salary= sheet.cell(2,2).value
		# designation = sheet.cell(3,3).value
		# dateofjoining= sheet.cell(4,4).value

		employee_id = sheet.cell_value(1,1)
		age = sheet.cell_value(1,2,)
		salary = sheet.cell_value(1, 3)
		designation = sheet.cell_value(1, 4)
		vDOJ = "01-01-2019"


		# Assign values from each row
		values = (employee_id, age, salary, designation, vDOJ)

		# Execute sql Query
		cur.execute(query, values)

myconn.commit()
# Close the database connection
myconn.close()



