import openpyxl

book1 = openpyxl.open("book1.xlsx", read_only=True)
sheet = book1.active
book2 = openpyxl.open("book2.xlsx", read_only=True)
sheet2 = book2.active
book3 = openpyxl.open("book3.xlsx", read_only=True)
sheet3 = book3.active
print(sheet["A1"].value)
print(sheet2["A1"].value)
print(sheet3["A1"].value)
books = openpyxl.Workbook()
sheet4 = books.active
sheet4['A1'] = sheet3["A1"].value
sheet4['A2'] = sheet2["A1"].value
sheet4['A3'] = sheet["A1"].value
books.save("books.xlsx")
books.close()
