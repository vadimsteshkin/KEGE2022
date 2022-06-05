q=0
ma=444445
k=[int(i) for i in open('17_2.txt')]
m=max([i for i in k if i%19==0])
for i in range(len(k)-1):
    if k[i]>m or k[i+1]>m:
        q+=1
        ma=min(ma,k[i]+k[i+1])
print(q,ma)