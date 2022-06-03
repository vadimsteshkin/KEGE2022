from itertools import *
q=0
for i in product("школа", repeat=5):
    k=''.join(i)
    if k.count('а')!=0 or k.count('о')!=0:
        q+=1

print(q)