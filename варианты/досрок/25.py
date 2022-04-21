from itertools import *
for i in product('0123456789',repeat=2):
    k='12345'+str(i[0])+'6'+str(i[1])+'8'
    if int(k)<10**9 and int(k)%17==0:
        print(k,int(k)//17)
