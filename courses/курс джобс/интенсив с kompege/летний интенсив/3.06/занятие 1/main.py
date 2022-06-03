from itertools import *
for x,y,w,z in product(range(2),repeat=4):
    if (x<=y) and not(y==w) and(z<=x):
        print(w,z,x,y)