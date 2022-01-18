from itertools import *
k='123456789'
o=0
k=list(combinations_with_replacement(k,r=9))
print(k)
for i in k:
    if i[0]!='5' and i.count('2')==2:
        o+=1
print(o)