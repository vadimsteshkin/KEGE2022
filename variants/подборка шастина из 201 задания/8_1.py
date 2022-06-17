from itertools import *
q=0
for i in product('ШКОЛА',repeat=3):
    k=''.join(i)
    if k.count("К")==1:
        q+=1
print(q)