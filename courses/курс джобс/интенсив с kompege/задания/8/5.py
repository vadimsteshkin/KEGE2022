from itertools import *
q=0
for i in product('ЩОГБА', repeat=6):
    k=''.join(i)
    q+=1
    if k=='ОБЩАГА':
        print(q)