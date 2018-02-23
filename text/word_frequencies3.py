# File: word_frequencies3.py
# Usage:  1) python word_frequencies2.py a filename  --- sort entries alphabetically
#         2) python word_frequencies2.py f filename  --- sort entries by frequency

import sys
import frequency_table as FT


def get_data(filename):
  f = open(filename, "r")
  data = f.read()
  f.close()
  return data

def run(args):
    data = get_data(args[2]).lower()

    lines = data.split("\n")
    string = " ".join(lines)
    words_ = string.split(" ")
    words = list(filter(lambda x: x != '', words_))

    frequencies = FT.frequency_table(words).items()

    if sys.argv[1] == 'a':
      frequencies.sort(key=(lambda x: x[0]))
    else:
      frequencies.sort(key=(lambda x: -x[1]))

    print [len(lines), len(words), len(data)]
    for item in frequencies:
      print item

def print_message():
    print "Usage: python word_freq a filename    # or"
    print "       python word_freq f filename    #"
    print ""
    print "  First alternative for alphabetically sorted table"
    print "  Second alternative for table sorted by frequency"


if len(sys.argv) == 3:
    run(sys.argv)
else:
    print_message()    
