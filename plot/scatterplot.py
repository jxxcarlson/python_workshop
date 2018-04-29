# File: scatterplot.py

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)

N = 400

x = np.random.rand(N)
u = np.random.normal(0,.35,N)

def f(x,u):
    return  x + 8*x*x*(1-x)*(1-x)*u

y = f(x,u)

plt.scatter(x, y )

plt.savefig("scatter.png")
plt.show()
