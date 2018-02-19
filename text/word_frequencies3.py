# File: word_frequencies2.py
# Usage:  1) python word_frequencies2.py a filename  --- sort entries alphabetically
#         2) python word_frequencies2.py f filename  --- sort entries by frequency

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

def get_data(filename):
  f = open(filename, "r")
  data = f.read()
  f.close()
  return data


def run(args):
    data = get_data(args[2])
    lines = data.split("\n")
    string = " ".join(lines)
    words = string.split(" ")

    frequencies = frequency_table(words).items()

    if sys.argv[1] == 'a':
      frequencies.sort()
    else:
      frequencies.sort(key=(lambda x: -x[1]))

    print [len(lines), len(words), len(data)]
    print ""
    for item in frequencies:
      print item

print sys.argv

if len(sys.argv) == 3:
    run(sys.argv)
else:
    print "Usage: python word_freq a filename    # for alphabetically sorted frequency table"
    print "       python word_freq f filename    # for a table sorte by frequency"
