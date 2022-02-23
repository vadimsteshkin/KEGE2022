k=input()
l=sum([int(i) for i in k[0:3]])
s=sum([int(i) for i in k[3:6]])
if l==s:
    print('YES')
else:
    print('NO')