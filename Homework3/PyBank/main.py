import csv
import os

csv_path = os.path.join(
    r'D:\UCI Data Analytics Bootcamp\UCI\Homework3\PyBank\raw_data', 'budget_data_1.csv')

with open(csv_path, 'r', newline='', encoding='utf-8') as csv_file:

    budget_data = csv.DictReader(csv_file, delimiter=',')

    months = []
    revenue = []
    total_months = 0
    total_revenue = 0

    for line in budget_data:
        # Count months
        total_months += 1

        # Append dates into list
        months.append(line['Date'])

        # Format revenue
        line['Revenue'] = int(line['Revenue'])

        # Append revenue into list
        revenue.append(line['Revenue'])

        # Add to total revenue
        total_revenue = total_revenue + line['Revenue']

    print(len(months))
    print(sum(revenue))
    print("Total Months: " + str(total_months))
    print("Total Revenue: " + str(total_revenue))
