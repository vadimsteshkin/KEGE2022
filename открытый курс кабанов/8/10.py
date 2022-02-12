from itertools import *
q=0
for i in product('ВИШНЯ',repeat=6):
    s=''.join(i)
    if s.count('В')<=1 and s[0]!='Ш' and s[-1] not in 'ЯИ':
        q+=1
print(q)