def prime(n):  
    for i in range(2,int(pow(n,0.5))+1):
        if n%i==0:
            return 1
    return 0
q=0
for i in range(55556,55777):
    if prime(i)==0:
        q+=1
print(q)
