k=open('26_3.txt')
m=sorted([int(x) for x in k.readlines()[1::]],reverse=True)
q=0
su=600
s=0
k.close()
for i in m:
    k=600-m[i]
    while k>min(m):
        f=True
        while f:
            if k in m:
                m[i]+=k
                m.remove(k)
                f=False
            else:
                k-=1
    print(k)
print(q,s)