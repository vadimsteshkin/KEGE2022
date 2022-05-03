from itertools import *
q=0
for i in product('СОН', repeat=6):
    k=''.join(i)
    if 'С' not in k[3::] and k.count('С') in [0,1,3]:
        q+=1
print(q)