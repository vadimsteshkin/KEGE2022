f=open('24 (1).txt').readline()
O=0
for i in range(len(f)-3):
    if f[i]=='Z' and f[i+2]=='R' and f[i+3]=='O':
        O+=1
    print(f[i]+f[i+2]+f[i+3])
print(O)