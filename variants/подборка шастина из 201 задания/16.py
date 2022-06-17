from itertools import *
for x,y,w,z in product(range(2),repeat=4):
    if (not(y<=w) or (x==z) or x)==0:
        print(z,y,w,x)