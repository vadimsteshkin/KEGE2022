from itertools import *
q=0
for i in product('AB123',repeat=8):
    s=''.join(i)
    if (s.count('A')+s.count('B'))==2:
        q+=1
print(q)