from itertools import *
q=0
m=['ac','ae','ea','ec','ca','ce','bd','bf','db','fb','fd','df']
for i in range(10):
    for j in range(10):
        if i!=j and i%2==j%2:
            m.append(str(i)+str(j))
print(m)
for i in permutations([], r=5):
    k=''.join(i)
    if k[0]!='0' and all(i not in k for i in m):
        q+=1



