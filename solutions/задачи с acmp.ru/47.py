def d(n):
    s=set()
    for i in range(1,int(pow(n,0.5))+1):
        if n%i==0:
            s|={i,n//i}
    return s
k=int(input())
s=sum([int(x) for x in str(k)])
n=d(k)
print(n)
lst=[[s,k]]
for i in n:
    lst.append([sum([int(x) for x in str(i)]),i])
print(max(lst)[1])
