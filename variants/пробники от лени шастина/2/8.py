from itertools import *
q=0
a=[str(i)*3 for i in range(9)]
for i in product('012345678',repeat=7):
    k=''.join(i)
    if k[0]!='0' and k[-1] not in ['3','4','7'] and all(i not in k for i in a):
        q+=1
print(q)