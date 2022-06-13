from itertools import *
for x,y,w,z in product(range(2),repeat=4):
    if ((x<=y) or not(w<=z))==0:
        print(z,y,w,x)