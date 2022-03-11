for i in range(int(input())):
    n,m=map(int,input().split())
    print(int(19*m + (n + 239)*(n + 366) / 2)) 