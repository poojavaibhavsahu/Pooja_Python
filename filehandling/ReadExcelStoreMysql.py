import xlrd
import pymysql

# Open the workbook and define the worksheet
book = xlrd.open_workbook("data.xlsx")

sheet = book.sheet_by_index(0)

# Establish a MySQL Connection
myconn = pymysql.connect (host="localhost", user="root", passwd="root", db="mydatabase")

# Get the cursor, which is used to traverse the database, line by line
cur = myconn.cursor()

# Create the INSERT INTO sql query
query = "INSERT INTO student1 (name, rollno, marks) VALUES (%s, %s, %s)"

# Create a for loop to iterate through each row in the xls file, starting from row 2
for r in range(1, sheet.nrows):
    name = sheet.cell(r,0).value
    rollno = sheet.cell(r,1).value
    marks = sheet.cell(r,2).value

    # Assign values from each row
    values = (name, rollno, marks)

    # Execute sql query
    cur.execute(query, values)
# Close the cursor
cur.close()

#Commit the transaction
myconn.commit()
#Close the database connection
myconn.close()

