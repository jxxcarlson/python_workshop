# File: random_string

import random

def randchar(str):
    return random.choice(list(str))

def randstring(n, str):
    output = ""
    for k in range(0, n):
        output = output + randchar(str)
    return output

def nonsense(n):
    return randstring(n, 'abcdefghijklmnopqrstuvwxyz')

def password():
    return nonsense(4) + '.' + randstring(4, '0123456789')
