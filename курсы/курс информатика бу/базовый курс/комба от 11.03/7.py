from itertools import *
q=0

k=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
for i in product(k,repeat=7):
    s=''.join(i)
    if max