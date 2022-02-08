from itertools import *
k=input()
lst=list()
for i in permutations(k):
    _=''
    for j in i:
        _+=j
    lst.append(_)
lst=sorted(lst)
print(lst[lst.index(k)+1])
