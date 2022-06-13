from itertools import *
for x,y,w,z in product(range(2),repeat=4):
    if ((w==z) or (x and not(y)) or w)==0:
        print(z,y,x,w)