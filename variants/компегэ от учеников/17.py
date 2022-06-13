f=[int(i) for i in open('17.txt')]
a=[]
q=0
k=max([i for i in f if int(pow(i,0.5))==pow(i,0.5)])*3
for i in range(len(f)-1):
    if int(pow(f[i]*f[i+1],0.5))==pow(f[i]*f[i+1],0.5) and min(f[i],f[i+1])<k:
        q+=1
        a.extend([f[i],f[i+1]])
print(q,max(a)+min(a))