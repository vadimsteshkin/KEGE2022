k=open('26_3.txt')
m=sorted([int(x) for x in k.readlines()[1::]],reverse=True)
q=0
s=0
while len(m)>0:
    for i in range(len(m)):
        if s+m[i]<=600:
            s+=m[i]
            m[i]=0
    m=[x for x in m if x!=0]
    q+=1
    print(s)
    s=0
print(q)
