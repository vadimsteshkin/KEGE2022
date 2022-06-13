f=open('24_8.txt').readline()
k=[i for i in range(len(f)) if f[i]=='A']
m=0
for i in range(len(k)-2):
    m=max(m,k[i+2]-k[i])
print(m-1)
