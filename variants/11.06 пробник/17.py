f=[int(i) for i in open('17.txt')]
ma=max([i for i in f if i%11==0])
q=0
m=100000000000000000
for i in range(len(f)-1):
    if max(f[i],f[i+1])>ma:
        q+=1
        m=min(m,f[i]+f[i+1])
print(q,m)