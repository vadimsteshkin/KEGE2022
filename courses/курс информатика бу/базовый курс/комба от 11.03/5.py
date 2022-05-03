from itertools import *
q=0
for i in product('КАРНВЕ',repeat=6):
    k=''.join(i)
    if k.count('А')<3 and k.count('В')==1:
        q+=1
print(q)