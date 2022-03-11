k=[int(x) for x in open('17_17.txt')]
s=[x for x in k if x%10==0]
l=min(s)+max(s)
m=0
q=0
for i in range(len(k)-1):
    if k[i]+k[i+1]<l:
        q+=1
        m=max(m,k[i]+k[i+1])
print(q,m)