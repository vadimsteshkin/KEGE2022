from itertools import *
k=''
o=0
for i in product('АБИКОЛУН',repeat=8):
    k=''
    for j in i:
        k+=j
    if k.count('ЛН')==0 and k.count('КН')==0 and k.count('КЛ')==0 and k.count('БЛ')==0 and k.count('БН')==0 and k.count('БК')==0 and k.count('ОУ')==0 and k.count('ИУ')==0 and k.count('АО')==0 and k.count('АУ')==0 and k.count('ИО')==0 and k.count('АИ')==0 and k.count('А')<2 and  k.count('Б')<2 and k.count('И')<2 and k.count('О')<2 and k.count('К')<2 and k.count('Л')<2 and k.count('У')<2 and k.count('Н')<2:
        o+=1
print(o)
    