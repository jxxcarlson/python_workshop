# File: scatterplot_from_file.py

import numpy as np
import matplotlib.pyplot as plt
import sys
import json

file = open(sys.argv[1], 'r')
data_string = file.read()
file.close()

xs, ys = json.loads(data_string)

plt.scatter(xs, ys)
plt.savefig("scatter.png")
plt.show()
