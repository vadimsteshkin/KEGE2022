q=0
ma=0
k=[int(i) for i in open('17_1.txt')]
m=sum(k)/len(k)
for i in range(len(k)-2):
    s=[k[i],k[i+1],k[i+2]]
    s.sort()
    if s[-1]>m and s[-2]>m:
        q+=1
        ma=max(ma,sum(s))
print(q,ma)