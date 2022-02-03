s=0
i=0
f=open('26.txt').readlines()
k=f[0].split()
f=sorted([int(x) for x in f[1::]],reverse=True)
while int(k[1])>i:
    s+=f[i]
    i+=1
print(s,f[i])
