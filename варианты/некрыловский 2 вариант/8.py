from itertools import *
u=0
for i in product('КРOТ', repeat=6):
    m = list(i)
    k=' '
    for j in m:
        k += j
    if k.count('O')==1:
        u+=1
print(u)
