k=int(input())
if k<0:
    m=0
    for l in range(1,k-1,-1):
        m+=l
if k==0:
    m==1
else:
    m = (1+k)*k//2
print(m)