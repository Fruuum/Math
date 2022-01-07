import matplotlib.pyplot as plt
import numpy as np
sums = []
for i in range(1001):
    x = np.random.rand(5)
    sums.append(sum(x))
    i += 1

columns = 10
n, bins, patches = plt.hist(sums, columns)
plt.xlabel("intervals")
plt.ylabel("frequency")
plt.show()
