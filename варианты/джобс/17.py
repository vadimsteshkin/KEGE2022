f=[int(i) for i in open('17.txt')]
q=0
m=0
s=sum([int(str(i)[0]) for i in f])
for i in range(len(f))-1:
    if f[i]*f[i+1]>s:
        q+=1
        m=max(m,f[i]+f[i+1]) 
print(q,m)