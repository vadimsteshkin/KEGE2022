from itertools import *
q=0
for i in product('ВИШНЯ',repeat=6):
    k=''.join(i)
    if k[0]!='Ш' and k[-1] not in ['И','Я'] and k.count('В')<2:
        q+=1
print(q)