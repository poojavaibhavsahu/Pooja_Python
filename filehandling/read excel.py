import xlrd
#define the location of the file
loc=("abc.xlsx")
#to open the workbook
wb = xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)
#for row 0 and coloumn 0

#for sheet in wb.sheets():
for rowidx in range(sheet.nrows):
    row = sheet.row(rowidx)
    for colidx, cell in enumerate(row):
         print("condition name is: ",cell.value )

         rowidx= rowidx + 1
