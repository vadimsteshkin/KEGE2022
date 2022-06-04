f=open('26_7.txt')
l,m,n=map(int,f.readline().split())
for i in range(n):
    a.append(map(int,f.readline()))
print(a)