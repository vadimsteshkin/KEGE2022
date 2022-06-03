f=[int(i) for i in open('17_1.txt')]
m=max([i for i in f if i%2])
q=0
ma=100000
for i in range(len(f)-1):
    if 2*(f[i]+ f[i+1])>m:
        q+=1
        ma=min(ma,f[i]+f[i+1])
print(q,ma)