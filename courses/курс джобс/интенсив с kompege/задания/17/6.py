q=0
ma=9999999
k=[int(i) for i in open('17_6.txt')]
m=max([i for i in k if i%111==0])
for i in range(len(k)-1):
    if (k[i]%10==7 or k[i+1]%10==7) and (k[i]>m or k[i+1]>m):
        q+=1
        ma=min(ma,k[i]+k[i+1])
print(q,ma)