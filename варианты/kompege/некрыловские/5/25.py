def prime(n):
    for i in range(2,int(pow(n,0.5))+1):
        if n%i==0:
            return False
    return True
o=0
o1=0
for i in range(10**7,1111111111111):
    m=prime(i)
    if m==True:
        o+=1
        print(i,abs(10**7-i))
    if o==5:
        break
for j in range(10**7,11,-1):
    d=prime(j)
    if d==True:
        o1+=1
        print(j,abs(10**7-j))
    if o1==5:
        break
