import sys
import math
import numpy as np
import re

## WORD ANALYSIS

def depunctuate(word):
    return re.sub(r"(.*)[\"\.,:;!?]", r"\1", word)

def normalize(word):
    return depunctuate(word).lower()

def words(text):
    words = text.split()
    return map(normalize, words)

def word_lengths(data):
    return map(len, words(data))

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

def relative_frequencies(data):
    frequency_table = frequencies(data)
    relative_frequency_table = rescale(frequency_table)
    return relative_frequency_table.values()

## GEOMETRY

def distance(u, v):
    d = 0
    for i in range(0, len(u)):
        delta = u[i] - v[i]
        d = d + delta*delta
    return math.sqrt(d)

def norm(u):
    sum = 0
    for element in u:
        sum = sum + element*element
    return math.sqrt(sum)

def scalarproduct(a, u):
    return map(lambda x: a*x, u)

def normalize_vector(u):
    return scalarproduct(1/norm(u), u)

def normalized_distance(u,v):
    return distance(normalize_vector(u), normalize_vector(v))

def dot(u,v):
    sum = 0
    for i in range(0, len(u)):
        sum = sum + u[i]*v[i]
    return sum

def angle(u,v):
    uu = normalize_vector(u)
    vv = normalize_vector(v)
    return (180/np.pi)*np.arccos(dot(uu,vv))


## GET DATA AND ANALYZE IT

file_name_1 = sys.argv[1]
file_name_2 = sys.argv[2]

print
print file_name_1
print file_name_2

file_1 = open(file_name_1,"r")
file_2 = open(file_name_2,"r")

data_1 = file_1.read()
data_2 = file_2.read()

file_1.close()
file_2.close()

frequencies_1 = rescale(frequencies(word_lengths(data_1))).values()
frequencies_2 = rescale(frequencies(word_lengths(data_2))).values()

normalized_frequencies_1 = normalize_vector(frequencies_1)
normalized_frequencies_2 = normalize_vector(frequencies_2)

print normalized_frequencies_1
print
print normalized_frequencies_2
print
print
print norm(normalized_frequencies_1)
print norm(normalized_frequencies_2)
print


print "angle: ", round(angle(normalized_frequencies_1, normalized_frequencies_2), 1)
print
