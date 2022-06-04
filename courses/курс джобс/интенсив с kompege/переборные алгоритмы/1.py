f=open('27-B.txt')
q=0
m=f.readline()
k=[int(i) for i in f]
for i in range(len(k)):
    for j in range(i+1,len(k)):
        if (max(k[i],k[j])-min(k[i],k[j])) %13==0 and k[i]*k[j]%2==0:
            q+=1
print(q)