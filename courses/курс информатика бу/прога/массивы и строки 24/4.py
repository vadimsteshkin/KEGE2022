f=open('24zadachi__kma.txt').readline()
q=0
for i in range(len(f)-2):
    if f[i]==f[i+2] and f[i]=='X' and f[i+1]!='X':
        q+=1

print(q)