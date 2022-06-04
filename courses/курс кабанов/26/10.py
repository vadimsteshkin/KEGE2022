f=open('26_10.txt')
n=map(int,f.readline())
a=[int(i) for i in f]
b=[0 for i in range(10_000_001)]
a.sort()
s=0
for i in a:
   s+=i
   print(s)
   b[s]=1
print(max(b))
b=[b.index(i)+1 for i in b if i==0]
print(len(b),max(b))