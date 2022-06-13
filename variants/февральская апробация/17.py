f=[int(i) for i in open('17.txt')]
m=max([i for i in f if i%11==0])
q=0
p=-11111111
for i in range(len(f)-1):
    if (f[i] *f[i+1])%11==0 and (f[i]+f[i+1])<=m:
        q+=1
        p=max(p,f[i]+f[i+1])
print(q,p)