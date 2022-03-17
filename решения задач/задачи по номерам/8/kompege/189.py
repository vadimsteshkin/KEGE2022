from itertools import *
q=0
for i in product('КРОТ',repeat=6):
    s=''.join(i)
    if s.count('О')==1:
        q+=1
print(q)