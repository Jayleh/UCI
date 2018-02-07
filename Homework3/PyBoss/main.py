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
    emp_id = []
    first_name = []
    last_name = []
    dob = []
    ssn = []
    state = []

    for emp in emp_data:
        # Parse columns with parse functions
        emp['Name'] = split_name(emp['Name'])
        emp['DOB'] = parse_date(emp['DOB'])
        emp['SSN'] = parse_ssn(emp['SSN'])
        emp['State'] = parse_state(emp['State'])

        # Append values to lists
        first_name.append(emp['Name'][0])
        last_name.append(emp['Name'][1])
        emp_id.append(emp['Emp ID'])
        dob.append(emp['DOB'])
        ssn.append(emp['SSN'])
        state.append(emp['State'])

    # Declare new csv file path
    new_csv_path = os.path.join(os.getcwd(), 'PyBoss\\Employee Data', 'employee_data1.csv')

    with open(new_csv_path, 'w', newline='', encoding='utf-8') as output_csv:
        # Fieldnames
        headers = ['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State']

        csv_writer = csv.writer(output_csv, delimiter=',')

        # Write headers
        csv_writer.writerow(headers)

        # Write rows with list items
        for i in range(0, len(emp_id)):
            csv_writer.writerow([emp_id[i]] + [first_name[i]] +
                                [last_name[i]] + [dob[i]] + [ssn[i]] + [state[i]])
