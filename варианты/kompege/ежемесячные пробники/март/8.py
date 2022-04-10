
from math import prod
from timeit import repeat

from itertools import *
a='0123456789'
q=0
for i in product(a,repeat=5):
    k=''.join(i)
    if k[0] not in['0','4','3','7']:
        if len([0 for j in a if k.count(j*3)])==0:
            q+=1
        else:
            print(k)
print(q)