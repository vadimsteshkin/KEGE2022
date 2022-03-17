from itertools import *
q=0
for i in permutations('ПОКА',r=4):
    s=''.join(i)
    if 'ПП' not in s and 'КК' not in s and 'ПК' not in s and 'КП' not in s and 'АА' not in s and 'ОО' not in s and 'ОА' not in s and 'АО' not in s:
        q+=1
        print(s)

print(q)