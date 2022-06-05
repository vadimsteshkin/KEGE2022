q=0
ma=0
k=[int(i) for i in open('17_4.txt')]
m=[i for i in k if i%10==4]
n=max(m)+min(m)
for i in range(len(k)-1):
    if (k[i]+k[i+1])<n:
        q+=1
        ma=max(ma,k[i]+k[i+1])
print(q,ma)