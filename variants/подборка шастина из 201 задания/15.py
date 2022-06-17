from itertools import *
for x,y,w,z in product(range(2),repeat=4):
    if (not(x<=z) or (y==w) or not(y))==0:
        print(x,z,y,w)