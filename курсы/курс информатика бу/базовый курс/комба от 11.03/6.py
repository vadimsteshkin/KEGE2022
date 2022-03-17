from itertools import *
q=0
for i in permutations('КАРИНА',r=6):
    k=''.join(i)
    if k[0] not in['А','И']:
        q+=1
print(q)