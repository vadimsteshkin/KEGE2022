k=open('24.txt').read()
m=0
for i in range(len(k)-2):
    if k[i]=='Z' and k[i+2]=='R' and k[i+3]=='O':
        m+=1
print(m)
alpha='asdfghjklzxcvbnmpoiuytrewq'.upper()
p=0
for _ in alpha:
    o='Z'+ _+ 'R'+'O'
    p+=k.count(o)
print(p)