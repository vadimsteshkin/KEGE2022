k=open('24_2.txt').readline()
m=0
lst=[]
for i in range(len(k)-1):
    f=True
    q=1
    j=i
    while f and j!=len(k)-1:
        if int(k[j])%2==int(k[j+1])%2:
            q+=1
        else:
            f=False
            m=max(q,m)
        j+=1
print(m)
