from itertools import *
for x,y,w,z in product(range(2),repeat=4):
    if ((x and  not y) or(y==z) or not w)==0:
        print(x,w,z,y)