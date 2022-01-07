import numpy as np
r, b, z, n = 0, 0, 0, 0
for i in range(0, 100):
    x = np.random.randint(1, 38)
    n += 1
    if x <= 18:
        r += 1
    elif x == 37:
        z += 1
    else:
        b += 1
if n == r + b + z:
    print('True')
print(f'red - {r}, black - {b}, zero - {z}')
