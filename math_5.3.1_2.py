import numpy as np
import math
k1, k2, n = 0, 0, 10000
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
x = a + b + c + d
num_tests = 4
num_rez_2 = 2
num_rez_3 = 3
for i in range(0, n):
    if x[i] == 2:
        k1 += 1
    elif x[i] == 3:
        k2 += 1
print(f'успешных попыток - {k1}, число попыток - {n}, вероятность повторного выпадения орла - {k1/n}')
print(f'успешных попыток - {k2}, число попыток - {n}, вероятность тройного выпадения орла - {k2/n}')

#: проверка по формуле Бернулли
C1 = math.factorial(num_tests) / (math.factorial(num_rez_2) * math.factorial(num_tests - num_rez_2))
C2 = math.factorial(num_tests) / (math.factorial(num_rez_3) * math.factorial(num_tests - num_rez_3))
print(f'Pn(2) = {C1 / 2 ** num_tests}')
print(f'Pn(3) = {C2 * (1/2) ** num_rez_3 * (1/2) ** (num_tests - num_rez_3)}')
