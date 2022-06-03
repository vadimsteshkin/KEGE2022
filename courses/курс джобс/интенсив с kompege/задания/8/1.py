from itertools import *
q=0
for i in product('ГАФНИЙ',repeat=4):
    k=''.join(i)
    if k[0]!='Й' and ((k.count('А')+k.count('И'))>0):
        q+=1
print(q)