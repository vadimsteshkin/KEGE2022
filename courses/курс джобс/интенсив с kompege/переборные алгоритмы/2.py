f=open('27-A2.txt')
q=0
m=f.readline()
k=[int(i) for i in f]
for i in range(len(k)):
    for j in range(i+1,len(k)):
        if (k[i]+k[j]) %10==0:
            q+=1
print(q)