f=open('27-B4.txt')
q=0
m2=0
m1=0
m=f.readline()
k=[int(i) for i in f]
for i in range(len(k)):
    for j in range(i+1,len(k)):
        if (k[j]%2==0 and k[j]>m1) and (k[i]+k[j])%2:
            q+=1
            m2=max(m2,k[j])
            m1 = max(k[i], m1)
        if (k[j]%2 and k[j]>m2) and (k[i]+k[j])%2:
            q+=1
            m1=max(k[j],m1)
            m2 = max(m2, k[i])
print(q)