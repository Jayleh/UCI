import csv
import os

csv_path = os.path.join(
    r'D:\UCI Data Analytics Bootcamp\UCI\Homework3\PyBank\raw_data', 'budget_data_1.csv')

with open(csv_path, 'r', newline='', encoding='utf-8') as csv_file:

    budget_data = csv.DictReader(csv_file, delimiter=',')

    total_months = 0
    total_revenue = 0

    for line in budget_data:
        total_months += 1
        line['Revenue'] = int(line['Revenue'])
        total_revenue = total_revenue + line['Revenue']

    print("Total Months: " + str(total_months))
    print("Total Revenue: " + str(total_revenue))
