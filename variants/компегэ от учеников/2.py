from itertools import *
for a,b,c,d in product(range(2),repeat=4):
    if (b<=(a and c or d and not a))==0:
        print(b,d,a,c)
