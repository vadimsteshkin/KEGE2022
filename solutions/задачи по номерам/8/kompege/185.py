from itertools import *
q=0
for i in product('КУМА',repeat=5):
    s=''.join(i)
    if s[0] in 'КМ' and s[-1] not in 'КМ':
        q+=1
print(q)