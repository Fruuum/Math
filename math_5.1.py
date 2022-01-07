import numpy as np
for i in range(0, 100):
    a = input()
    x = np.random.randint(1, 38)
    if x <= 18:
        print("red")
    elif x == 37:
        print("zero")
    else:
        print("black")
