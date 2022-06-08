f=[int(i) for i in open('1.txt').readline()]
q=1
m=0
for i in range(len(f)-1):
    print(f[i],f[i+1],q)
    if f[i]>=f[i+1]:q+=1
    else: q=1
    m=max(q,m)
print(m)