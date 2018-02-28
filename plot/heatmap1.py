import matplotlib.pyplot as plt
import numpy as np

a = np.random.random((5, 5))
print a
plt.imshow(a, cmap='hot', interpolation='nearest')
plt.show()
