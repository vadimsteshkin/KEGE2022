k=open('26_2.txt').readlines()
m=sorted([int(x) for x in k])
lst=[]
l=[]
l.append(0)
while len(m)>0:
    lst.append(max(m))
    m.remove(max(m))
    while len(m)>0 and(sum(l)+min(m))<sum(lst) :
        l.append(min(m))
        m.remove(min(m))
print(len(lst),len(l)-1)
    
        