f=[int(i) for i in open('27_A.txt')][1::]
q=0
for i in range(len(f)-1):
    for j in range(i+1,len(f)):
        m=sum(f[i:j+1])
        if m%67==0:
            q=max(q,m)
print(q)
