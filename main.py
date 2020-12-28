import openpyxl
import csv
import os

directory = r'/Users/andrew/Downloads/Excel/'
lwr_exten = '.xlsx'

for filename in os.listdir(directory):
    if filename.endswith(lwr_exten):
        wb = openpyxl.load_workbook(directory + filename)
        sh = wb.active
        name = filename.replace(lwr_exten, ".csv")
        with open(directory + name, 'w', newline="") as f:
            col = csv.writer(f)
            for row in sh.rows:
                col.writerow([cell.value for cell in row])
    else:
        continue

# Works as of 12-27-20, untested with .xls files.