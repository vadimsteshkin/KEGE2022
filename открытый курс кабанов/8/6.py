from itertools import *
k=''
o=0
for i in product('ИГРОК',repeat=5):
    k=''
    for j in i:
        k+=j
    if k.count('РОК')==0 and k[0]!="К" and k.count('И')<2 and  k.count('Г')<2 and k.count('Р')<2 and k.count('О')<2 and k.count('К')<2:
        o+=1
print(o)
    