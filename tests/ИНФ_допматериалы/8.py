from itertools import *
q=0
for i in product('АБРТЫ',repeat=5):
    q+=1
    k=''.join(i)
    if k.count('Й')+k.count("АА")==0:
        print(q,k)
        break