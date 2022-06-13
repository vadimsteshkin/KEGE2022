from  itertools import *
for x,y,w,z in product(range(2),repeat=4):
    if (not(x<=y) or ((not(w))<=(not(z))) or w)==0:
        print(x,y,w,z)