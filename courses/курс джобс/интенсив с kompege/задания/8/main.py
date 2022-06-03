from itertools import *
q=0
for i in product('012345678', repeat=7):
    k=''.join(i)
    if k[0] not in['0','2','4','6'] and (not(k[-1]==k[-2]==k[-3])):
        q+=1
print(q)