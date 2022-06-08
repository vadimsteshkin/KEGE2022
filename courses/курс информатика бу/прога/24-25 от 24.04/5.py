f=open('5.txt').readline()
a=[]
s=set()
for i in range(len(f)-2):
    if f[i]==f[i+2]:
        a.append(f[i+1])
        s.add(f[i+1])
k=max(s,key=lambda x:a.count(x))
print(k,a.count(k))