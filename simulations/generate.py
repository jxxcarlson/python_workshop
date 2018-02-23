# File generate.py
import random

def generate(initial_value, n):
    x = initial_value
    k = 0
    output = [x]
    while k < n:
        k = k + 1
        x = x + 2*random.randint(0,1) - 1
        output.append(x)
    return output
