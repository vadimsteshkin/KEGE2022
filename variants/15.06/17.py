f=[int(i) for i in open('17.txt')]
m=min([i for i in f if i%103==0])
q=0
ma=0
for i in range(len(f)-1):
    if (f[i]+f[i+1])%2==0 and abs(f[i]-f[i+1])%m==0:
        q+=1
        ma=max(f[i]+f[i+1],ma)
print(q,ma)