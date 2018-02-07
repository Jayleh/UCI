import os
import csv
from datetime import datetime as dt
from us_state_abbrev import us_state_abbrev

os.chdir(r'D:\UCI Data Analytics Bootcamp\UCI\Homework3')
csv_path = os.path.join(os.getcwd(), 'PyBoss\\0 raw_data', 'employee_data1.csv')

# csv_path = os.path.join('0 raw_data', 'employee_data1.csv')


def split_name(name):
    if name == '':
        return None
    else:
        name = name.split(" ")
        return name


def parse_date(date):
    if date == '':
        return None
    else:
        return dt.strptime(date, '%Y-%m-%d').strftime('%m/%d/%Y')


def parse_ssn(ssn):
    if ssn == '':
        return None
    else:
        ssn = "***-**" + ssn[-5:]
        return ssn


def parse_state(state):
    if state == '':
        return None
    else:
        for key, value in us_state_abbrev.items():
            if state == key:
                state = value
                return state


with open(csv_path, 'r', newline='', encoding='utf-8') as input_csv:

    # Read csv file as data frame
    csv_reader = csv.DictReader(input_csv, delimiter=',')

    emp_data = list(csv_reader)
    first_name = []
    last_name = []

    for emp in emp_data:
        emp['Name'] = split_name(emp['Name'])
        emp['DOB'] = parse_date(emp['DOB'])
        emp['SSN'] = parse_ssn(emp['SSN'])
        emp['State'] = parse_state(emp['State'])

        # Append first names to list
        first_name.append(emp['Name'][0])

        # Create new column with first name
        # first_name = emp['Name'][0]
        # emp['First Name'] = first_name

        # Append last names to list
        last_name.append(emp['Name'][1])

        # Rename Name to First Name
        # emp['First Name'] = emp.pop('Name')

        # Create new column with last name
        # last_name = emp['Name'][1]
        # emp['Last Name'] = last_name

    print(emp_data[0])
    print(first_name[0:4])
    print(last_name[0:4])

    # Declare new csv file path
    new_csv_path = os.path.join(os.getcwd(), 'PyBoss\\Employee Data', 'employee_data1.csv')

    with open(new_csv_path, 'w') as output_csv:
        # Fieldnames
        headers = ['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State']

        csv_writer = csv.DictWriter(output_csv, fieldnames=headers, delimiter=',')

        # for row in emp_data:
        #     csv_writer.writerow(row)
