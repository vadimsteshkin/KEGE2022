from itertools import *
q=0
for i in product('катер', repeat=3):
    k=''.join(i)
    if k.count('р')>1:
        q+=1
print(q)