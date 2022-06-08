from  itertools import *
q=0
for i in product('АБРТЫ',repeat=5):
    q+=1
    k=''.join(i)
    if k.count('Ы')==0 and k.count('АА')==0:
        print(q)