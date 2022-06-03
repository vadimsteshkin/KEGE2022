k=7**202+49**102-7**20
m=0
while k>0:
    if k%7==6:
        m+=1
    k//=7
print(m)