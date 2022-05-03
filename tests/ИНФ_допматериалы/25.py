from itertools import *
for i in product('0123456789',repeat=2):
    k=''.join(i)
    s='12345'+k[0]+'7'+k[1]+'8'
    if int(s)%23==0:
        print(s,int(s)//23)