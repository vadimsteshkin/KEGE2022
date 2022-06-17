from itertools import *
for x,y,w,z in product(range(2),repeat=4):
    if ((not(x))<=y) and ((not(y))==z) and w:
        print(z,y,x,w)