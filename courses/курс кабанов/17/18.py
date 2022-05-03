k=[int(x) for x in open('17_18.txt')]
m=0
q=0
for i in range(len(k)-1):
    if (k[i]%9==0 and oct(k[i+1])[-1]=='3' and k[i+1]%9!=0) + (k[i+1]%9==0 and oct(k[i])[-1]=='3' and k[i]%9!=0)==1:
        q+=1
        m=max(max(k[i],k[i+1]),m)
        print(k[i],k[i+1])
print(q,m)