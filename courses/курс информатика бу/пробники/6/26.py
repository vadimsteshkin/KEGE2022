q=0
fi=open('26.txt')
lst=[]
q=0
o=0
n,s=map(int, fi.readline().split())
for i in range(n):
    l,p,k=fi.readline().split()
    lst.append([l,int(p),int(k)])
lst=sorted(lst)
for i in lst:
    o+=1
    if q<s:
        break
    q+=i[1]*i[2]
print(p,q)