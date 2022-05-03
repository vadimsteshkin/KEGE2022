from itertools import *
q=0
for i in product('ГАФНИЙ',repeat=4):
    s=''.join(i)
    if s[0]!="Й" and('А' in s or 'И' in s):
        q+=1
print(q)