from itertools import *
for x,y,w,z in product(range(2),repeat=4):
    if (not(x<=w) or (y==z) or y)==0:
        print(z,x,w,y)