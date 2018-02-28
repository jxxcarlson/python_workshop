
from matplotlib.mlab import griddata
import matplotlib.pyplot as plt
import numpy as np

from math import cos
fig = plt.figure
pi = 3.1416

alpha = 0.7
phi_ext = 2 * pi * 0.5

def flux_qubit_potential(phi_m, phi_p):
    return 2.0 + alpha - 2.0 * cos(phi_p)*cos(phi_m) - alpha * cos(phi_ext - 2*phi_p)


phi_m = np.linspace(0, 2*pi, 100)
phi_p = np.linspace(0, 2*pi, 100)
X,Y = np.meshgrid(phi_p, phi_m)
Z = flux_qubit_potential(X, Y).T

fig, ax = subplots()

p = ax.pcolor(X/(2*pi), Y/(2*pi), Z, cmap=cm.RdBu, vmin=abs(Z).min(), vmax=abs(Z).max())
cb = fig.colorbar(p)
