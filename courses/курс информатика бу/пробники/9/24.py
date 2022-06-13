f=open('24.txt').readline()
m=[0 for i in range(26)]
a='QWERTYUIOPASDFGHJKLZXCVBNM'
for i in range(len(f)-1):
    if f[i]=='Z':m[a.index(f[i+1])]+=1
print(a[(m.index(max(m)))])
