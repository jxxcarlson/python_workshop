import sys
import re
import numpy as np
import math

## TEXT MANIPULATIONS FUNCTIONS

def depunctuate(word):
    return re.sub(r"(.*)[\.,:;!?]", r"\1", word)

def normalize(word):
    return depunctuate(word).lower()

def words(text):
    words = text.split()
    return map(normalize, words)

def word_lengths(words):
    return map(len, words)

def add_entry(dictionary, key):
    if key in dictionary:
        dictionary[key] = dictionary[key] + 1
    else:
        dictionary[key] = 1

def frequencies(data):
    freq = dict()
    for i in range(0,21):
        freq[i] = 0
    for datum in data:
        add_entry(freq, datum)
    return freq

def rescale(dictionary):
    total = float(sum(dictionary.values()))
    new_dictionary = dict()
    for key in dictionary.keys():
        new_dictionary[key] = dictionary[key]/total
    return new_dictionary

def angle(u,v):
    uu = unit_vector(u)
    vv = unit_vector(v)
    return (180/np.pi)*np.arccos(dot(uu,vv))
## ANGLES BETWEEN VECTORS

def norm(u):
    sum = 0
    for element in u:
        sum = sum + element*element
    return math.sqrt(sum)

def scalarproduct(a, u):
    return map(lambda x: a*x, u)

def unit_vector(u):
    return scalarproduct(1/norm(u), u)

def dot(u,v):
    sum = 0
    for i in range(0, len(u)):
        sum = sum + u[i]*v[i]
    return sum

## GET THE DATA AND ANALYZE IT

def analyze_text(file_name):
    f = open(file_name,"r")
    data = f.read()
    f.close()
    relative_frequency_dictionary = rescale(frequencies(word_lengths(words(data))))
    frequency_vector = relative_frequency_dictionary.values()
    return frequency_vector

rfv1 = analyze_text(sys.argv[1])
rfv2 = analyze_text(sys.argv[2])

text_angle = angle(rfv1, rfv2)

print
print "File 1:", sys.argv[1]
print "File 2:", sys.argv[2]
print "Angle: ", round(text_angle,1)
print
