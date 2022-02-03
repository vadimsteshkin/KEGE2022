k=open('27-B.txt')
o=k.readline()
lst=[]
ls=[]
for i in range(int(o)):
    m=[int(x) for x in k.readline().split()]
    lst.append(max(m))
    ls.append(max(m)-min(m))
print(sum(lst))