_=input()
k=[int(x) for x in input().split()]
s=[int(x) for x in k if x%2]
i=[int(x) for x in k if x%2==0]
print(*s)
print(*i)
if len(s)>len(i):
    print('NO')
else:print('YES')