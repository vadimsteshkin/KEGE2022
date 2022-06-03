from itertools import *
q=0
for i in permutations('калий', r=5):
    k=''.join(i)
    if k.count('иа')==0 and k[0]!='й':
        q+=1
print(q)