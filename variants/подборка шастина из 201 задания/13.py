from itertools import *

for x, y, w, z in product(range(2), repeat=4):
    if not (y <= (x == w)) and (z <= x):
        print(w, x, y, z)
