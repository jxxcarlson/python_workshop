# statistics.py -- word statistics
# example: $ python statistics.py statistics.py computes
# statistics on the file statistics.py:
# $ python statistics.py statistics.py
# 72 words
# 44 unique words
# redundancy = 38%

import sys

def get_content():
  file = open(sys.argv[1])
  return file.read()

def unique(L):
  U = []
  for element in L:
    if element not in U:
      U.append(element)
  return U

def run():

  text = get_content()
  text = text.lower()
  words = text.split()

  n_words = len(words)
  n_unique_words = len(unique(words))

  f = float(n_unique_words)/n_words
  f = 1 - f
  f = int(f*100)

  message = str(n_words)+" words"
  print(message)

  message = str(n_unique_words)+" unique words"
  print(message)

  message = "redundancy = "+str(f)+"%"
  print(message)

run()
