f=open('26_6.txt')
k=f.readline()
a=[int(i) for i in f]
b=set(a)
m=0
for i in b:
    m=max(m,a.count(i))
print(len(b),m)