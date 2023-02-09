import sys
from collections import Counter

def count_words(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        # read the file content and split it into words
        words = file.read().lower().split()
        # count the number of occurrences of each word
        word_counts = Counter(words)
        # sort the word counts in descending order
        sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
        # print each word and its count
        for word, count in sorted_word_counts:
            print(f"{word}: {count}")

if __name__ == '__main__':
    filename = sys.argv[1]
    count_words(filename)

