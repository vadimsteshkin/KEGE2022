from itertools import *
q=0
for i in product('МЕТРО',repeat=4):
    s=''.join(i)
    if s[0] in 'МТР' and s[-1] not in 'МТР':
        q+=1
print(q)