f=open('24_2.txt').readline()
f=[int(i) for i in f]
q=1
m=0
for i in range(len(f)-1):
    if f[i]%2==f[i+1]%2:
        q+=1
    else:
        m=max(m,q)
        q=1
print(m)