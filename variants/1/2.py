from itertools import *
for a,b,c,d in product(range(2),repeat=4):
    if ((a and b)==(not(c))) and( b<=d):
        print(c,a,d)