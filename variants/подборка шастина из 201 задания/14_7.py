k=3*16**2018-2*8**1028-3*4**1100-2**1050-2022
q=0
while k>0:
    q+=(k%4==3)
    k//=4
print(q)