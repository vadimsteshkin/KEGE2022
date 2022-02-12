k,n=list(map(int,input().split()))
print(n // k + int(not(n % k == 0)), n % k if n % k != 0 else k)
