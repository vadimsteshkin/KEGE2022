from itertools import *
b='13579'
a='02468'
q=0
for i in product('0123456789',repeat=6):
    o=''
    for k in i:
        o+=k
    if o[0]!="0":
        for u in range(len(o)-2):
            if (not(o[u] in b and o[u+1] in b)) and  (not(o[u] in a and o[u+1] in a)):
                q+=1
                print(o)
print(q)