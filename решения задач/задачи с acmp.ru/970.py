k=sorted([int(x) for x in input().split()])
if max(k)==k[-3]+k[-2]:
    print('YES')
elif min(k) == k[-1]+k[-2]:
    print('YES')
elif k[-2]==k[-1]+k[-3]:
    print('YES')
else:print('NO')