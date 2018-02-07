import os

os.chdir(r'D:\UCI Data Analytics Bootcamp\UCI\Homework3')
txt_path = os.path.join(os.getcwd(), 'PyParagraph\\0 raw_data', 'paragraph_1.txt')

# txt_path = os.path.join('0 raw_data', 'paragraph_1.txt')

with open(txt_path, 'r') as input_txt:

    # Read csv file as data frame
    para = input_txt.read()

    print(para)
