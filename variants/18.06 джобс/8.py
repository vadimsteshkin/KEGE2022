from itertools import *
q=0
for i in product('EKHOB',repeat=5):
    q+=1
    k=''.join(i)
    if k.count('H')==k.count('K')==2:
        print(q,k)