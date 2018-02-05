import csv
import os

os.chdir(r'D:\UCI Data Analytics Bootcamp\UCI\Homework3')
csv_path = os.path.join(os.getcwd(), 'PyBank\\raw_data', 'budget_data_1.csv')


def mean(x):
    return float(sum(x) / (len(x)))


with open(csv_path, 'r', newline='', encoding='utf-8') as csv_file:

    # Read csv file as dictionary
    budget_data = csv.DictReader(csv_file, delimiter=',')

    # Create lists
    months = []
    revenue = []
    monthly_rev_chg = []

    # Loop through budget data
    for line in budget_data:
        # Format revenue
        line['Revenue'] = int(line['Revenue'])

        # Append dict values into lists
        months.append(line['Date'])
        revenue.append(line['Revenue'])

    # Loop thru zipped revenue lists
    for i, j in zip(revenue[:-1], revenue[1:]):
        # Append to monthly revenue change list
        monthly_rev_chg.append(j - i)
    # (numpy) monthly_rev_chg = np.diff(revenue)
    # (list comprehension) monthly_rev_chg = [j - i for i, j in zip(revenue[:-1], revenue[1:])]

    # Declare variables
    total_months = len(months)
    total_revenue = sum(revenue)
    avg_rev_chg = mean(monthly_rev_chg)
    great_inc = max(monthly_rev_chg)
    great_dec = min(monthly_rev_chg)

    # Instantiate index counter
    index = 0
    for i in monthly_rev_chg:
        index += 1
        if i == great_inc:
            # Declare month of greatest increase
            great_inc_month = months[index]
        elif i == great_dec:
            # Declare month of greatest increase
            great_dec_month = (months[index])

    print("Financial Analysis\n----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total Revenue: ${total_revenue}")
    print("mean Revenue Change: $" + str(round(avg_rev_chg, 2)))
    print(f"Greatest Increase in Revenue: {great_inc_month} (${great_inc})")
    print(f"Greatest Decrease in Revenue: {great_dec_month} (${great_dec})")

    # Declare text file path
    txt_path = os.path.join(os.getcwd(), 'PyBank', 'Financial Analysis.txt')

    with open(txt_path, 'w') as txt_file:

        # Write to text file
        txt_file.write("Financial Analysis\n----------------------------\n")
        txt_file.write(f"Total Months: {total_months}\n")
        txt_file.write(f"Total Revenue: ${total_revenue}\n")
        txt_file.write("mean Revenue Change: $" + str(round(avg_rev_chg, 2)) + "\n")
        txt_file.write(f"Greatest Increase in Revenue: {great_inc_month} (${great_inc})\n")
        txt_file.write(f"Greatest Decrease in Revenue: {great_dec_month} (${great_dec})\n")
