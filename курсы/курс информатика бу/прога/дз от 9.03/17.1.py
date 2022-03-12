from itertools import *
q=0
m=0
k=[int(x) for x in open('17__rd9.txt')]
for i in k:
    if i %12==0:
        q+=1
    else:
        m+=1
print(q*(q-1)+q*m,)