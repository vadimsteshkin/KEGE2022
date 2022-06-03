from itertools import *
q=0
for i in permutations("дейкстра", r=6):
    k=''.join(i).replace('д','.').replace('к','.').replace('с','.').replace('т','.').replace('р','.')
    if k.count('й')==1 and  "й."  in k:
        q+=1
print(q)