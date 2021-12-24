import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.mplot3d import Axes3D

fig = figure()
ax = Axes3D(fig)
X = np.arange(-25, 25, 5)
Y = np.arange(-25, 25, 5)
X, Y = np.meshgrid(X, Y)
Z2 = 8 - 2*X - 3*Y
Z1 = -2*(X+5) - (Y+10) * 3
ax.plot_surface(X, Y, Z1)
ax.plot_surface(X, Y, Z2)
show()

fig = figure()
ax = Axes3D(fig)
X = np.arange(-100, 50, 1)
Y = np.arange(-50, 100, 1)
X, Y = np.meshgrid(X, Y)
Z = X**2 - Y**2
ax.plot_surface(X, Y, Z)
show()
