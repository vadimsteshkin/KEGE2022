from itertools import *
q=0
for i in product('01234',repeat=6):
    if i[-1]!='3' and i[-1]!='4' and i[0]!='1' and i[0]!='0':
        q+=1
print(q)