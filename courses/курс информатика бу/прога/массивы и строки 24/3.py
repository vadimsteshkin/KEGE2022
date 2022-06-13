f=open('24zadachi__kma.txt').readline().replace('XYZ','*')
q=0
m=0
for i in range(len(f)):
    if f[i]=='*':
        q+=3
    else:
        if q>0:
            if f[i]=='X':
                q+=1
                if f[i+1]=='Y':
                    q+=1
        m=max(m,q)
        q=0
print(m)