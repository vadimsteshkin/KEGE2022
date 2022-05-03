from itertools import *
q=0
for i in permutations('БИНТЕГЬ',r=7):
    s=''.join(i)
    if s[-1]!='Ь' and (s.count('ИЬЕ') + s.count('ЕЬИ'))==0:
        q+=1
print(q)