q=0
fi=open('26.txt')
lst=[]
n,s=map(int, fi.readline().split())
for i in range(n):
    l,p,k=fi.readline().split()
    lst.append([l,int(p),int(k)])
while s+<=q: