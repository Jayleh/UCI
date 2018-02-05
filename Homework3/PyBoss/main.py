import csv
import os

os.chdir(r'D:\UCI Data Analytics Bootcamp\UCI\Homework3')
csv_path = os.path.join(os.getcwd(), 'PyBoss\\raw_data', 'employee_data1.csv')

with open(csv_path, 'r', newline='', encoding='utf-8') as csv_file:

    # Read csv file as dictionary
    emp_data = csv.DictReader(csv_file, delimiter=',')

    for line in emp_data:
        print(line)
