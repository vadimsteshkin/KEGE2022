s=0
for x in range(1,100000):
    k=7**500+7**200-7**50-x
    if k<0:
        break
    m=0
    while k>0:
        m+=k%7
        k//=7
    s=max(s,m)
    print(m,x)
print(m)