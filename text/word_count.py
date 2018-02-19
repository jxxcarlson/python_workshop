# File: word_count

import sys

f = open(sys.argv[1], "r")
data = f.read()
f.close()

lines = data.split("\n")
string = " ".join(lines)
words = string.split(" ")

print [len(lines), len(words), len(data)]
