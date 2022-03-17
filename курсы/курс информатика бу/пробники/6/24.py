k=open('24.txt').read()
m=0
k=k.replace('RR', 'R R').split()
for i in k:
    m=max(m,len(i)-i.count('RR'))
print(m)