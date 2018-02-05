import csv
import os

os.chdir(r'D:\UCI Data Analytics Bootcamp\UCI\Homework3')
csv_path = os.path.join(os.getcwd(), 'PyPoll\\raw_data', 'election_data_1.csv')

with open(csv_path, 'r', newline='', encoding='utf-8') as csv_file:

    # Read csv file as dictionary
    elect_data = csv.DictReader(csv_file, delimiter=',')

    Torres_count = 0

    for row in elect_data:
        if row['Candidate'] == 'Torres':
            Torres_count += 1

    print(Torres_count)
