# File: word_frequencies3.py
# Usage:  1) python word_frequencies2.py a filename  --- sort entries alphabetically
#         2) python word_frequencies2.py f filename  --- sort entries by frequency

import sys
import frequency_table as FT
from entropy import entropy
from round_off import round_off
import re


def get_data(filename):
  f = open(filename, "r")
  data = f.read()
  f.close()
  return data





def run(filename):
    data = get_data(filename).lower()
    data = re.sub(r'[!?.:;,-]', '', data)

    lines = data.split("\n")
    string = " ".join(lines)
    words_ = string.split(" ")
    words = list(filter(lambda x: x != '', words_))

    frequencies = FT.frequency_table(words)
    frequency_items = frequencies.items()

    entropy_of_text = entropy(frequencies)

    print 'lines:   ' + str(len(lines))
    print 'words:   ' + str(len(words))
    print 'chars:   ' + str(len(data))
    print "entropy: " + str(round_off(entropy_of_text,2))


def print_message():
    print "Usage: python text_entropy.py  filename"


if len(sys.argv) == 2:
    run(sys.argv[1])
else:
    print_message()
