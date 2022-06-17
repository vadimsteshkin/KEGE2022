from itertools import *

a = []


def f(s, e, x):
    q = 410 <= x <= 823
    p = 254 <= x <= 800
    a = s <= x <= e
    return (p and (not (a))) <= q


ox = [i / 4 for i in range(824 * 4)]
for z, y in combinations(ox, 2):
    if all(f(z, y, x) for x in ox):
        a.append(y - z)
print(min(a))
