f=open('24_1.txt').readline()
q=1
m=0
for i in range(len(f)-1):
    if f[i]!=f[i+1]:
        q+=1
    else:
        m=max(m,q)
        q=1
print(m)