k=open('27B_3.txt')
t=[]
p=[]
for i in range(int(k.readline())):
    m=int(k.readline())
    if m% 65==0:
        
    if m%5==0:
        p.append(m)
    elif m%13==0:
        t.append(m)
    
print(p,t)
print(len(p)*len(t))