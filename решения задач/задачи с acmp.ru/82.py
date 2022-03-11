input()
k=[int(x) for x in input().split()]
print(*sorted(set([int(x) for x in input().split() if int(x) in k])))
