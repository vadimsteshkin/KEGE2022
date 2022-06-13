from itertools import *
q=0
for i in product('0123456',repeat=7):
    k=''.join(i)
    if k[0] not in ['0','3','5'] and not('22' in k and '44' in k):
        q+=1
print(q)