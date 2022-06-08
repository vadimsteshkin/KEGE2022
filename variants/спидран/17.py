f=open('17.txt')
f=[int(i) for i in f]
q=0
m=0
for i in range(len(f)-1):
    if (f[i]*f[i+1])%14!=0:
        q+=1
        m=max(m,f[i]+f[i+1])
print(q,m)