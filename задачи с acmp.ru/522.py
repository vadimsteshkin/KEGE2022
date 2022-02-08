_=input()
k=[int(x) for x in input().split()]
u=[int(x) for x in input().split()]
if set(k)==set(u):
    print(1)
else:print(0)