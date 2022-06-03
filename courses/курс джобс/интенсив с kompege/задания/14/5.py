k=2**103+4**98-8**20
m=0
while k>0:
    if k%8==7:
        m+=1
    k//=8
print(m)