# File: scatter_make_data.py

import numpy as np
import matplotlib.pyplot as plt
import json
import sys

def round_off(x, digits):
    factor = 10**digits
    return round(x*factor)/factor

# Fixing random state for reproducibility
np.random.seed(19680801)

N = int(sys.argv[2])

x = np.random.rand(N)
u = np.random.normal(0,.35,N)

def f(x,u):
    return  x + 8*x*x*(1-x)*(1-x)*u

y = f(x,u)

x = map(lambda u: round_off(u, 3), x)
y = map(lambda u: round_off(u, 3), y)

data = [list(x), list(y)]

file = open(sys.argv[1], 'w')
file.write(json.dumps(data))
file.close()
