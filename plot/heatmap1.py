import matplotlib.pyplot as plt
import numpy as np

a = np.random.random((10, 10    ))
print a
plt.imshow(a, cmap='hot', interpolation='nearest')
plt.show()
