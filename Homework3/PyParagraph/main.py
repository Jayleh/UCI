import os
import re

# os.chdir(r'D:\UCI Data Analytics Bootcamp\UCI\Homework3')
# txt_path = os.path.join(os.getcwd(), 'PyParagraph\\0 raw_data', 'paragraph_1.txt')

# Path to read text file
txt_path = os.path.join('0 raw_data', 'paragraph_1.txt')


def mean(x):
    return float(sum(x) / (len(x)))


with open(txt_path, 'r') as txt_data:
    # Read text file
    paragraph = txt_data.read().replace("\n", " ")

    # Split paragraph by spaces
    para_split = paragraph.split(' ')

    # Declare variables
    word_count = len(para_split)
    letter_count_word = []

    for word in para_split:
        # Append length of each word into list
        letter_count_word.append(len(word))

    # Calculate average letter count per word
    avg_letter_count = mean(letter_count_word)

    # Split paragraph by sentences into a list
    sentence_split = re.split("(?<=[.!?]) +", paragraph)

    # Get number of sentences
    sentence_count = len(sentence_split)

    # Create list for word count for each sentence
    word_count_sent = []

    for sentence in sentence_split:
        # Append sentence lengths to list
        word_count_sent.append(len(sentence.split(" ")))

    avg_sentence_len = mean(word_count_sent)

    summary = (
        f"Paragraph Analysis\n------------------\n"
        f"Approximate Word Count: {word_count}\n"
        f"Approximate Sentence Count: {sentence_count}\n"
        f"Average Letter Count: {avg_letter_count:.5f}\n"
        f"Average Sentence Length {avg_sentence_len:.1f}\n"
    )

    print(summary)

# Declare text file path
# output_txt_path = os.path.join(os.getcwd(), 'PyParagraph\\Paragraph Analysis', 'paragraph_1.txt')
output_txt_path = os.path.join('Paragraph Analysis', 'paragraph_1.txt')

with open(output_txt_path, 'w') as txt_file:

    txt_file.write(summary)
