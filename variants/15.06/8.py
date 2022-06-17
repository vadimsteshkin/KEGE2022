from itertools import *
q=0
for i in product('DEINPTBR',repeat=4):
    q+=1
    k=''.join(i)
    if len(set(k))==4 and (k.count('R')+k.count('E'))==0:
        print(q)