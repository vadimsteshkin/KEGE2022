from itertools import *
q=0
for i in product('0123456789',repeat=3):
    s=''.join(i)
    f=True
    for j in range(len(s)-1):
        if s[j]>s[j+1]:
            f=False
    if f==True and s[0]!='0':
        q+=1
print(q)