q=0
mi=9999999
ma=0
k=[int(i) for i in open('17_7.txt')]
s=max(k)
for i in range(len(k)-2):
    if (k[i]+k[i+1]+k[i+2])<=s:
        q+=1
        ma=max(ma,k[i],k[i+1],k[i+2])
        mi=min(mi,k[i],k[i+1],k[i+2])
print(q,mi+ma)