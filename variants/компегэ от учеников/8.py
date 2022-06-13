from itertools import *
a=[]
for i in product('AIKLMB',repeat=6):
    k=''.join(i)
    a.append(k)
q=[]
for i in permutations('AIKLMB',r=6):
    i=''.join(i)
    q.append(i)
for i in q:
    s=i[::-1]
    print(s,i)
    if max([i.count(j) for j in i])==1 and i[0]=='K' and k[-1]=='B' and abs(a.index(s)- a.index(i))==26655:
        print(a.index(i)+1)
        break