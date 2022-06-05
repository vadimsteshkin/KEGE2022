q=0
ma=0
k=[int(i) for i in open('17_5.txt')]
m=max([i for i in k if i%11==0])
for i in range(len(k)-1):
    if (k[i]*k[i+1])%11==0 and (k[i]+k[i+1])<=m:
        q+=1
        ma=max(ma,k[i]+k[i+1])
print(q,ma)