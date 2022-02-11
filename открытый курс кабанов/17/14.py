m=0
q=0
k=[int(x) for x in open('17_14.txt')]
s=sum(k)/len(k)
for i in range(len(k)-2):
    if (k[i]>s) + (k[i+1]>s)+(k[i+2]>s)>1:
        q+=1
        m=max(k[i]+k[i+1]+k[i+2],m)
print(q,m)