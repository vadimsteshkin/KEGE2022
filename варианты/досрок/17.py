f=[int(i) for i in open('17.txt').readlines()]
q=0
s=0
m=min([i for i in f if i%17==0])
for i in range(len(f)-1):
    if (f[i]*f[i+1])%m==0:
        q+=1
        s=max(f[i]+f[i+1],s)
print(q,s)