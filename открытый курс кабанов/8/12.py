from itertools import *
q=0
for i in product('ГЕПАРД',repeat=5):
    s=''.join(i)
    if s[0]!='А' and s[-1]!='Е' and s.count("Г")==1:
        q+=1
print(q)