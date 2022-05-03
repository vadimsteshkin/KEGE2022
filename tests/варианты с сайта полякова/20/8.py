from itertools import *
q=0
for i in permutations('ВАЙФУ', r=4):
    k=''.join(i)
    print(k)
    if k[0]!='Й' and 'ВФ' not in k and 'ФВ' not in k:
        q+=1
print(q)