from itertools import *
q=0
for i in product('ГАПАВИЙ',repeat=5):
    s=''.join(i)
    if s[0]!='Й' and s[-1]!='Й' and (s.count("ЙИ")+s.count("ИЙ")==0):
        q+=1
print(q)