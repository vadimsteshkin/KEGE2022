f=open('27B_9.txt')
f=[int(i) for i in f][1::]
a=[0]*2000
for i in f:
    if i<=2000:
        a[2000-i]+=1
q=0
for i in range(1,1000):
    q+=(a[i]*a[2000-i])
q+=(a[1000]*(a[1000]-1))//2
print(q)
m=0
for i in range(len(f)-1):
    for j in range(i+1,len(f)):
        if (f[i]+f[j])==2000:
            m+=1
print(m)