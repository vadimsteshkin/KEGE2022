k=open('24_3.txt').readline()
m=1
ma=0
for i in range(len(k)-1):
    if k[i]==k[i+1]:
        m+=1
    else:
        ma=max(m,ma)
        m=1
print(ma)