f=open('2.txt').readline().split('Z')
m=0
for i in range(len(f)-2):
   m=max(m,len(f[i]+f[i+1]+f[i+2])+2)
print(m)

