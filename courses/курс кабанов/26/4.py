f=open('26_4.txt')
n=int(f.readline())
a=[int(i) for i in f]
a.sort()
q=0
m=100000000
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if (a[i]+a[j])%2==0:
            sr=(a[i]+a[j])//2
            if a[2499]<sr<a[3750]:
                q+=1
                m=min(m,sr)
print(q,m)