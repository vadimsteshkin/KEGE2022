from itertools import *
q=0
a=[str(i)*3 for i in [0,1,2,3,4,5,6,7,8,9]]

for i in product('012345678',repeat=7):
    s=''.join(i)
    if s[-1] not in '347' and s[0]!='0' and len([i for i in a if i in s])==0:
        q+=1
print(q)