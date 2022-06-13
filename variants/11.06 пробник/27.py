f=open('27B.txt')
a=[]
q=0
m=0
s=1
st=0
n,k=map(int,f.readline().split())
a=[int(i) for i  in f]
for i in range(n):
    s+=a[i]
    q+=1
    if s<=k:
        m=max(m,q)
    else:
        while s>k:
            s-=a[st]
            q-=1
            st+=1
        m=max(m,q)

print(m)