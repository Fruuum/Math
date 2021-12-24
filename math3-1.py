from math import sqrt

x1 = (float(input("add x value: ")))
y1 = (float(input("add y value: ")))
z1 = (float(input("add z value: ")))

vct_length = sqrt(x1 ** 2 + y1 ** 2 + z1 ** 2)
print(f'vector length is {round(vct_length, 2)}')
