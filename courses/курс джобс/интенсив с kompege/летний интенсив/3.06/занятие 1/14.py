from itertools import *
q=0
for i in product('012345678',repeat=7):
    k=''.join(i)
    if k[0] not in ['0','3','7'] and ('00' not in k and '11' not in k and '22' not in k and '33' not in k and '44' not in k and '55' not in k and '66' not in k and '77' not in k and '88' not in k):
        q+=1
    else:print(k)
print(q)