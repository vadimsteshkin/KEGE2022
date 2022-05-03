from itertools import *
q=0
for i in permutations('ДЕЙКСТРА',r=6):
    s=''.join(i)
    if not('ЙЕ' in s or 'ЙА' in s) and s.count("Й")==1 and s[-1]!='Й':
        q+=1
print(q)