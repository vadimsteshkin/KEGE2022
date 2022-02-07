def d(n):
    s=set()
    for i in range(1,int(pow(n,0.5)+1)):
        if n%i==0:
            s|={n//i,i}
    if len(s)<3:
        return 0
    return sum(s)
def f(n):

    k='9'
    for i in range(len(n)):
        if k[-1]>=k[i]:
  
        else:
            return 0
    return 1 
print(f(92143))
