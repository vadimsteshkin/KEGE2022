f=open('27B_10.txt')
a=[]
c=0
n=0
for i in range(int(f.readline())):
    k=int(f.readline())
    if k%2:
        n=max(n,k)
    else:c=max(c,k)
print(c+n)