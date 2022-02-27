q=0
k=open('text4.txt').read()
for i in range(len(k)-2):
    if k[i]=='V' and k[i+2]=='V':
        q+=1
print(q)