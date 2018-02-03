import csv
import os
import numpy as np

csv_path = os.path.join(os.getcwd(), 'Pybank\\raw_data', 'budget_data_1.csv')

with open(csv_path, 'r', newline='', encoding='utf-8') as csv_file:

    budget_data = csv.DictReader(csv_file, delimiter=',')

    months = []
    revenue = []

    def average(x):
        return sum(x) / max(len(x))

    for line in budget_data:
        # Format revenue
        line['Revenue'] = int(line['Revenue'])

        # Append dict values into list
        months.append(line['Date'])
        revenue.append(line['Revenue'])

    # With using numpy
    chg_btwn_months = np.diff(revenue)
    # chg_btwn_months = [j - i for i, j in zip(revenue[:-1], revenue[1:])]

    total_months = len(months)
    total_revenue = sum(revenue)
    # avg_rev_chg =

    print(f"Total Months: {total_months}")
    print(f"Total Revenue: ${total_revenue}")
    print(revenue)
    print(chg_btwn_months)
    # print("Average Revenue Change: $" + str(average(chg_btwn_months)))
