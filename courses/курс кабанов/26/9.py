f=open('26_9.txt')
b=[]
for i in range(31):
    b.append([0]*8)
n=int(f.readline())
a=list(set([i for i in f]))
a.sort()
for i in a:
    y,m=map(int, i.split())
    b[y-1961][m-1]=1
print(sum([i.count(0) for i in b]))
for j in b:
    print(j)
    print(j.count(0),b.index(j)+1961)