k=8**1023+2**1024-3
m=0
while k>0:
    if k%2==1:
        m+=1
    k//=2
print(m)