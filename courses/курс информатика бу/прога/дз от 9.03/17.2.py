k=[int(x) for x in open('17__rd9.txt')]
q=0
m=0
for j in range(len(k)-1):
    for i in range(j+1,len(k)):
        if (k[i]*k[j])%34!=0:
            q+=1
            m=max(m,k[i]+k[j])
print(q,m)