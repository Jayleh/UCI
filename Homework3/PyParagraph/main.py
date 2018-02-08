import os
# import re

os.chdir(r'D:\UCI Data Analytics Bootcamp\UCI\Homework3')
txt_path = os.path.join(os.getcwd(), 'PyParagraph\\0 raw_data', 'paragraph_1.txt')

# txt_path = os.path.join('0 raw_data', 'paragraph_1.txt')


def mean(x):
    return float(sum(x) / (len(x)))


with open(txt_path, 'r') as input_txt:

        # Read text file
    para = input_txt.read()

    # Split paragraph by spaces
    para_no_space = para.split(' ')

    # Declare variables
    word_count = len(para_no_space)
    sentence_count = 0
    letter_count_word = []

    # re.split("(?&lt;=[.!?]) +", para)

    for word in para:
        if '.' in word:
            sentence_count += 1
        elif '!' in word:
            sentence_count += 1
        elif '?' in word:
            sentence_count += 1

    word_count_sent = []
    count = 0
    for word in para_no_space:
        letter_count_word.append(len(word))

    print(para_no_space)
    print('Paragraph Analysis\n-----------------')
    print(f'Approximate Word Count: {word_count}')
    print(f'Approximate Sentence Count: {sentence_count}')
    print(f'Average Letter Count: {round(mean(letter_count_word), 5)}')
    print('Average Sentence Length: ')
