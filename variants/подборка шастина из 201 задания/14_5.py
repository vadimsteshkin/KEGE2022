k=3*4**38+2*4**23+4**20+3*4**5+2*4**4+1
q=0
while k>0:
    q+=(k%16==0)
    k//=16
print(q)