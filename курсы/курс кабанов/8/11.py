from itertools import *
q=0
for i in product('ABCD',repeat=4):
    s=''.join(i)
    if 'DB'  not in s and 'DC'  not in s and 'DA'  not in s and 'CB'  not in s and 'CA'  not in s and'BA'  not in s:
        q+=1
        print(s)
print(q)