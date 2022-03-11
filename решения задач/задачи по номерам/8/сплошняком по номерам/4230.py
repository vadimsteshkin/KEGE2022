from itertools import *
 
q=0
for i in product('0123456789ABCDEF',repeat=5):
    k=''.join(i)
    s=''.join(sorted(i))
    if k==s and k[0]!='0':
        print(k)
        q+=1
print(q)