from itertools import *
q=0
for i in product('АБВГЭЮЯ',repeat=5):
    s=''.join(i)
    if s[0] in 'ЭЮЯ' and s[-1] in 'ЭЮЯ' and len(([i for i in s[1:4] if i in 'ЭЮЯ']))==0:
        print(s)
        q+=1
print(q)