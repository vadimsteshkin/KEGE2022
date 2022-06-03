from itertools import *
q=0
for i in product('пскаль', repeat=4):
    k=''.join(i)
    if k[0]!='ь' and  k.count("ьь")==0:
        q+=1
print(q)