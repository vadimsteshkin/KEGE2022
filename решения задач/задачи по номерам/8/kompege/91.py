from itertools import *
q=0
for i in product("ЕИЙКНОТ",repeat=7):
    s=''.join(i)
    if s.count("КОТ")>=1:
        q+=1
print(q)