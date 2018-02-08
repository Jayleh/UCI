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

    # Create list for word count for each sentence
    word_count_sent = []

    count = 0
    for word in para_no_space:
        # Append length of each word into list
        letter_count_word.append(len(word))

        # Increment count for each word
        count += 1

        # Loop to reset count at end of sentence
        if '.' in word:
            # Append word count of each sentence into list
            word_count_sent.append(count)

            # Reset count
            count = 0

    # print(para_no_space)
    # print(word_count_sent)
    print('Paragraph Analysis\n-----------------')
    print(f'Approximate Word Count: {word_count}')
    print(f'Approximate Sentence Count: {sentence_count}')
    print(f'Average Letter Count: {round(mean(letter_count_word), 5)}')
    print(f'Average Sentence Length: {mean(word_count_sent)}')

    # Declare text file path
    txt_path = os.path.join(
        os.getcwd(), 'PyParagraph\\Paragraph Analysis', 'paragraph_1.txt')

    with open(txt_path, 'w') as txt_file:

        txt_file.write('Paragraph Analysis\n-----------------\n')
        txt_file.write(f'Approximate Word Count: {word_count}\n')
        txt_file.write(f'Approximate Sentence Count: {sentence_count}\n')
        txt_file.write(f'Average Letter Count: {round(mean(letter_count_word), 5)}\n')
        txt_file.write(f'Average Sentence Length: {round(mean(word_count_sent), 1)}')
