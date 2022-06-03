f=[int(i) for i in open('17.txt')]
m=min([i for i in f if i%6==0])
q=0
ma=0
for i in range(len(f)-1):
    if f[i]%m==0 and f[i+1]%m==0:
        q+=1
        ma=max(ma,f[i]+f[i+1])
print(q,ma)