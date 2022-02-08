k=[int(x) for x in input().split()]
if k[0]+k[1]>=k[2]:
    print(sum(k)-2*k[2])
else:print('Impossible')