f=[i for i in open('3.txt').readline()]
q=1
m=0
s=0
for i in range(len(f)-1):
    if f[i]>f[i+1]:q+=1
    else: q=1
    if q>m:
        s=i-q+2
    m=max(q,m)
print(s+1)