import openpyxl
wb=openpyxl.load_workbook("2.xlsx")
print(wb)

sheet=(wb.active.title)
print(sheet)
actsht=wb.sheetnames
print(actsht)

data=wb["first"]["D16"].value
print(data)

data2=wb["second"]["C20"].value
print(data2)

