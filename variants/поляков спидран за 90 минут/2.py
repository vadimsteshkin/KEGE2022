from itertools import *
for x,y,w,z in product(range(2),repeat=4):
    if (((x<=w) or y and not(z)) and((y<=(not(z))) or x and not(w)))==0:
        print(z,x,y,x)