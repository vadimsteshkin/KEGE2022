input()
a=[int(i) for i in input().split()]
n=int(input())
for i in range(n):
    s,f=map(int,input().split())
    print(*a[s-1:f])
    
