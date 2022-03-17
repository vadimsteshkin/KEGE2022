from itertools import *
k=set()
for i in permutations('КВОВОВО',r=7):
    s=''.join(i)
    k.add(s)
print(len(k))