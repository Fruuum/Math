from matplotlib import pyplot as plt
import numpy as np

fig, ax = plt.subplots()

k1 = 1
k2 = 2
x = np.linspace(-5, 5, 100)
plt.plot(x, np.cos(k1*x))
plt.plot(x, np.cos(k2*x))

plt.show()
