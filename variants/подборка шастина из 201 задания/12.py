from itertools import *
for a,b,c,d in product(range(2),repeat=4):
    if ((not(a) and not(b)) or (b==c) or d)==0:
        print(c,d,b,a)