_=int(input())
k=[int(x) for x in input().split()]
s=0
for i in range(_):
    s+=k[i]-1
print(s+1)