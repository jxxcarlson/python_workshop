# File: word_frequencies1.py

import sys
import frequency_table as FT

f = open(sys.argv[1], "r")
data = f.read()
f.close()

lines = data.split("\n")
string = " ".join(lines)
words = string.split(" ")

print [len(lines), len(words), len(data)]
print FT.frequency_table(words)
