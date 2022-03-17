q=0
m=0 
k=[int(x) for x in open('17.txt')]
for i in range(len(k)-1):
    for j in range(i+1,len(k)):
        if (k[i]+k[j])%71==0 and (k[i]*k[j])%17==0:
            q+=1
            m=max(m,k[i]+k[j])
print(q,m)