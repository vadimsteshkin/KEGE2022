from itertools import *
q=0
for i in product('0123456',repeat=7):
    s=''.join(i)
    if s[0] not in '035' and ('22' not in s or '44' not in s):
        q+=1
print(q)