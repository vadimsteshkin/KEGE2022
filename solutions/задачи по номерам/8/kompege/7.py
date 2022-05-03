from itertools import *
q=0
for i in product('ШКОЛА',repeat=3):
    s=''.join(i)
    if s.count("К")==1:
        q+=1
print(q)