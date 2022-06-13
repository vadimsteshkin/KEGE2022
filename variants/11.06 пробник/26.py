k=sorted([list(map(int,i.split())) for i in open('26.txt')][1::])
f=[[]for i in range(10000)]
q=1
m=0
s=0
for i in k:
    f[i[0]].append(i[1])
for i in range(len(f)):
    f[i]=sorted(set(f[i]))
    for j in range(len(f[i])-1):
        if f[i][j]-f[i][j+1]==-1:q+=1
        else:
            m=max(q,m)
            q=1
    print(i,m)
