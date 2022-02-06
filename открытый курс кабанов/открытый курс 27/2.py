s=[]
l=[]
k=open('27A_2.txt')
for _ in range(int(k.readline())):
    m=int(k.readline())
    if m%7==0:
        s.append(m)
    else:
        l.append(m)
p=0
for i in range(len(s)):
    p+=i
print(len(s)*len(l)+p)