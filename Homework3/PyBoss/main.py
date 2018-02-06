import os
import pandas as pd

# os.chdir(r'D:\UCI Data Analytics Bootcamp\UCI\Homework3')
# csv_path = os.path.join(os.getcwd(), 'PyBoss\\0 raw_data', 'employee_data1.csv')

csv_path = os.path.join('0 raw_data', 'employee_data1.csv')

with open(csv_path, 'r', newline='', encoding='utf-8') as csv_file:

    # Read csv file as data frame
    df = pd.read_csv(csv_file, delimiter=',')
    
    print(df)
    