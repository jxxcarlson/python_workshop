import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 2.01, 0.01)
s = np.sin(np.pi*t) + (1.0/3.0)*np.sin(3*np.pi*t) + (1.0/5.0)*np.sin(5*np.pi*t)
abscissa = np.zeros(len(t))

plt.plot(t, s)
plt.plot(t, abscissa, color='black', linewidth=1.0 )

plt.savefig("fourier.png")
plt.show()
