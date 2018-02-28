

from math import log

def value_size(dictionary):
  size = 0
  for (key, value) in dictionary.items():
      size = size + value
  return size

def key_size(dictionary):
  return len(dictionary)

def log2(x):
  return log(x)/log(2)

def entropy(dictionary):
    h = 0
    n = float(value_size(dictionary))
    for key in dictionary:
        p = dictionary[key]/n
        h = h - p*log2(p)
    return h

# def entropy(frequencies):
#     h = 0
#
#     for word in frequencies:
