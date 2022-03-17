lst=[]
f=open('26_2944.txt')
s,n=map(int,f.readline().split())
for i in range(n):
    lst.append(int(f.readline()))
lst=sorted(lst)
q=0
res=0
while lst[q]+res<s:
    res+=lst[q]
    q+=1
res-=lst[q-1]
for m in reversed(lst):
    if m +res<=s:
        print(q,m)
        break
