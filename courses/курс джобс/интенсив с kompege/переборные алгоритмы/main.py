from itertools import *
f=open('27-A.txt')
q=0
k=[int(i) for i in f.readlines()][1::]
for i in combinations(k,r=2):
    if (max(i)-min(i))%13==0 and (i[0]*i[1])%2==0:
        q+=1
print(q)