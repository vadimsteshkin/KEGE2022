f=open('24_3.txt').readline()
q=1
m=0
for i in range(len(f)-2):
    if f[i+1]!=f[i] and f[i+1]!=f[i+2]:
        q+=1
    else:
        m=max(m,q)
        q=1
print(m-1)