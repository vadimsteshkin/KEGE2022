from itertools import *
for x,y,w,z in product(range(2),repeat=4):
    if not(w) and ((y or z) <=(y and not x)):
        print(w,z,y,x)