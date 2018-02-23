# File: word_frequencies2.py
# Usage:  1) python word_frequencies2.py a filename  --- sort entries alphabetically
#         2) python word_frequencies2.py f filename  --- sort entries by frequency

import sys
import frequency_table as FT

f = open(sys.argv[2], "r")
data = f.read()
f.close()

lines = data.split("\n")
string = " ".join(lines)
words = string.split(" ")

frequencies = FT.frequency_table(words).items()

if sys.argv[1] == 'a':
  frequencies.sort(key=(lambda x: x[0]))
else:
  frequencies.sort(key=(lambda x: -x[1]))

print [len(lines), len(words), len(data)]
for item in frequencies:
  print item
