from itertools import *
q=0
for i in product('АСВХ',repeat=5):
    s=''.join(i)
    if 'Х' not in  s[0:4]:
        print(s)
        q+=1
print(q)