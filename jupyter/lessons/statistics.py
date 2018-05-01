# Little statistics package

import math

def mean(data):
    return round(sum(data)/float(len(data)), 2)

def delta(data, center):
    return map(lambda x: x - center, data)

def deviation(data):
    return delta(data, mean(data))

def variance(data):
    squares = map(lambda x: x*x, deviation(data))
    return sum(squares)/len(data)

def stdev(data):
    return round(math.sqrt(variance(data)),2)
