from itertools import *
for x,y,w,z in product(range(2),repeat=4):
    if((x<=(y and not(z))) or w)==0:
        print(z,w,x,y)