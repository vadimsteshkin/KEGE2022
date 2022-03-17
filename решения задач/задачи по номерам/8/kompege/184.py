from itertools import *
q=0
for i in product('ТОК',repeat=6):
    s=''.join(i)
    if s[0]!='О':
        q+=1
print(q)