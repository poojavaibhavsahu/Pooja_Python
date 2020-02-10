import xlsxwriter
#create a workbook
wb=xlsxwriter.Workbook('pooja.xlsx')
#add a worksheet
worksheet=wb.add_worksheet()
#write a value in a sheel
worksheet.write('A1','Hello world')
print("success")
#close a workbook
wb.close()

