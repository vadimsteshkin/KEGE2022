k=input().split()
print(k)
s=int(k[0])-1
print(''.join([x for x in k[1] if k[1].index(x)!=s]))