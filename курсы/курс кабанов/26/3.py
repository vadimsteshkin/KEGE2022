k=open('26_3.txt')
m=sorted([int(x) for x in k.readlines()[1::]],reverse=True)
q=0
su=600
s=0
k.close()
for i in m:
    if s+i>600:
        for j in m:
            if s+j>600:
                w=m[m.index(j)-1]
                s+=w
                m.remove(w)
                break 
        s=0
        q+=1
        print(s)
    s+=i
       
print(q,s)