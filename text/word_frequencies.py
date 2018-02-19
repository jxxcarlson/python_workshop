# File: word_frequencies.py

import sys

def add_word(dictionary, word):
    if word in dictionary:
        dictionary[word] = dictionary[word] + 1
    else:
        dictionary[word] = 1

def frequency_table(words):
    frequencies = dict()
    for word in words:
        add_word(frequencies, word)
    return frequencies



f = open(sys.argv[1], "r")
data = f.read()
f.close()

lines = data.split("\n")
string = " ".join(lines)
words = string.split(" ")

print [len(lines), len(words), len(data)]
print frequency_table(words)
