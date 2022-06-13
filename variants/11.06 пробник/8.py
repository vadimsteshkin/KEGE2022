from itertools import *
q=0
for i in product('ABKLY',repeat=4):
    k=''.join(i)
    q+=1
    if all(k.count(x)<2 for x in k):
        print(q)