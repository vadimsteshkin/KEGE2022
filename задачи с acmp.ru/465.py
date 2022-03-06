from itertools import *
q=0
for i in product('01',repeat=int(input())):
    k=''.join(i)
    if '11' not in k:
        q+=1
print(q)