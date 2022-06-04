f=open('26_8.txt')
a=[0]*2500000
l,m,n=map(int,f.readline().split())
for i in range(n):
    k=list(map(int,f.readline().split()))
    a[k[1]:k[0]+1]=1
print(a)