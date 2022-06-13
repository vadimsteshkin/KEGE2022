f=[int(i) for i in open('17.txt')]
m=max(i for i in f if i%111==0)
q=0
mi=111111111
for i in range(len(f)-1):
    if max(f[i],f[i+1])>m and (f[i]%10==7 or f[i+1] %10==7):
        q+=1
        mi=min(f[i]+f[i+1],mi)
print(q,mi)