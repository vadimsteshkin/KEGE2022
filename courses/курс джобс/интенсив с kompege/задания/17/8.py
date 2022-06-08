q=0
ma=0
k=[int(i) for i in open('17_8.txt')]
s=sum(k)/len(k)
for i in range(len(k)-1):
    if (k[i]<s and k[i+1]<s) and (k[i]%10==9 or k[i+1]%10==9):
        q+=1
        ma=max(k[i]+k[i+1],ma)
print(q,ma)