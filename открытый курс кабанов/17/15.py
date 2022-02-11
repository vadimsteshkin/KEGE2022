k=[int(x) for x in open('17_15.txt')]
m=0
q=0
for i in k:
    if i%19==0:
        m=max(i,m)
s=1000000000000
for j in range(len(k)-1):
    if (k[j]>m)+(k[j+1]>m)>0:
        q+=1
        s=min(s,k[j]+k[j+1])
print(q,s)