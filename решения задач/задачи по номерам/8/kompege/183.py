from itertools import *
q=0
for i in product('ЛЕТО',repeat=4):
    s=''.join(i)
    if s[0] not in "ОЕ":
        q+=1
print(q)