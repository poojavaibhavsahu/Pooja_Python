import xlrd

loc=("abc.xlsx")
wb = xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)
xlRows=sheet.nrows
xlColumns=sheet.ncols
print(sheet.nrows)
print(sheet.ncols)

for i in range(xlRows):
    VEmpid=sheet.cell_value(2,0)
    Vage=sheet.cell_value(2,1)
    VSalary=sheet.cell_value(2,2)
    VDesignation=sheet.cell_value(2,3)
    vDOJ = "01-01-2019"
    print("Vale of emp id -",VEmpid)
    print("Value of Vage-" , Vage)
    print("Value of Emp Age -" , VSalary)
    print("Value of Emp VDesignation -", VDesignation)
    print("value of emp  vdoj_",vDOJ)
myconn.close()