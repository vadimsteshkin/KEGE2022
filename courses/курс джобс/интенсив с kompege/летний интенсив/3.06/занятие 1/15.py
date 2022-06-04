from itertools import *
q=0
for i in product('ЕЛНОСЦ',repeat=5):
    q+=1
    if i.count('Л')==0 and i.count('Е')<2:
        print(q)
        break

