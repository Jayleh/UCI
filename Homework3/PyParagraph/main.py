import os

os.chdir(r'D:\UCI Data Analytics Bootcamp\UCI\Homework3')
txt_path = os.path.join(os.getcwd(), 'PyParagraph\\0 raw_data', 'paragraph_1.txt')

# txt_path = os.path.join('0 raw_data', 'paragraph_1.txt')

with open(txt_path, 'r') as input_txt:

    # Read text file
    para = input_txt.read()

    # Split paragraph by spaces
    para = para.split(' ')

    # Declare variables
    word_count = len(para)
    sentence_count = 0

    for word in para:
        if '.' in word:
            sentence_count += 1

    print(para)
    print('Paragraph Analysis\n-----------------')
    print(f'Approximate Word Count: {word_count}')
    print(f'Approximate Sentence Count: {sentence_count}')
