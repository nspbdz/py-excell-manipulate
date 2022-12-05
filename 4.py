from openpyxl import load_workbook
 
#load excel file
workbook = load_workbook(filename="untitled.xlsx")
 
#open workbook
sheet = workbook.active
 
#modify the desired cell
sheet["B1"] = 100
 
#save the file
workbook.save(filename="saved1_file.xlsx")