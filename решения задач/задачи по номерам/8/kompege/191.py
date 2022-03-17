from itertools import *
q=0
for i in product('КАНТ',repeat=6):
    s=''.join(i)
    if s.count('К')==2:
        q+=1
print(q)