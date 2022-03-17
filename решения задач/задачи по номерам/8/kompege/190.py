from itertools import *
q=0
for i in product('ABCDX',repeat=4):
    s=''.join(i)
    if s.count('X')==1:
        q+=1
print(q)