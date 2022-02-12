from itertools import *
q=0
for i in permutations('ВАЙФУ',r=4):
    s=''.join(i)
    if s[0]!='Й' and not('ВФ' in s or 'ФВ' in s):
        q+=1
print(q)