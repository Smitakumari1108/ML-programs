#python program to load csv file 
import pandas as pd
import openpyxl

csv_file = "StudentDT.csv"
excel_file = "StudentDT.xlsx"


df_csv = pd.read_csv("C:/Users/smita/OneDrive/Desktop/ML Programs/student_data.csv")

print("CSV Data:")
print(f"File Name: {csv_file}")
print(df_csv.info())
print(df_csv.head())
workbook = openpyxl.load_workbook(excel_file)
worksheet = workbook["StudentDT"]
print("\n Excel Data:")
print(f"File Name: {excel_file}")

first_row = next(worksheet.iter_rows(min_row=1, max_row=1))

print("Column Names:")
for cell in first_row:
    print(cell.value)
