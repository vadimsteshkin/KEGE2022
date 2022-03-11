from itertools import *
k=''
o=0
for i in product('ЛОДКА',repeat=4):
    k=''
    for j in i:
        k+=j
    if k.count('О')>=2:
        o+=1
print(o)
    