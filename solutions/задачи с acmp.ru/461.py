input()
k=sorted([int(x) for x in input().split()])
print(sum([k[i]//2+1 for i in range(len(k)//2+1)]))
