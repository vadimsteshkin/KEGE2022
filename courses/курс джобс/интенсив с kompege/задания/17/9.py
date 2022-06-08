q=0
ma=-100000
k=[int(i) for i in open('17_9.txt')]
s=len([i for i in k if abs(i)<100])
for i in range(len(k)-1):
    if (k[i] + k[i + 1]) / 2>s:
        q+=1
        ma=max(ma,k[i]+k[i+1])
print(q,ma)