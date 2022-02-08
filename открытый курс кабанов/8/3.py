from itertools import *
k=''
o=0
for i in product('ПУЛЯ',repeat=6):
    k=''
    for j in i:
        k+=j
    if k.count('У')==2:
        o+=1
print(o)
    