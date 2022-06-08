from itertools import *
for x,y,w,z in product([0,1],repeat=4):
    if not(((not(x))==z) <=(y==(w or x))):
        print(y,x,w,z)