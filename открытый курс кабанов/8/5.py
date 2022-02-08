from itertools import *
k=''
o=0
for i in product('САЛО',repeat=6):
    k=''
    for j in i:
        k+=j
    if 0<k.count('О')<=3:
        o+=1
print(o)
    