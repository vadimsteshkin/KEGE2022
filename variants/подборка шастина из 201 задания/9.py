from itertools import *
for x,y,w,z in product(range(2),repeat=4):
    if (x or y) and not(y==z) and not(w):
        print(z,y,x,w)