lst=[]
f=open('26_2651.txt')
_=f.readline()
res=[]
a=set()
for o in range(int(_)):
    a.add((map(int,f.readline().split())))
a=sorted(a)
print(a)
q=0
m=0
for i in range(len(a)-1):
    if a[i][0]==a[i+1][0]:
        m+=1     
    else:
        res.append([8-m,a[i][0]])
        m=0