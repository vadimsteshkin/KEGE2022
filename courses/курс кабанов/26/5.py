f=open('26_5.txt')
n=f.readline()
a=[int(i) for i in f]
b=set(a)
m=0
q=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        k=a[i]+a[j]
        if k%2 and k in b:
            q+=1
            m=max(m,k)
print(q,m)