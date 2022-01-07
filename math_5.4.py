import itertools
n, m = 0, 0
for p in itertools.permutations('012', 2):
    n += 1
    print("".join(str(x) for x in p))

for r in itertools.combinations('01234', 3):
    m += 1
    print("".join(str(x) for x in r))
print(f'количество размещений - {n}, количество сочетаний - {m}')
