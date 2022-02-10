def d(k):
    n=0
    for i in range(1,int(n/2)+1):
        if k%i==0:
            n+=i
    return n
print(d(int(input())))
