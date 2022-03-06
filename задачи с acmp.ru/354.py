def p(n):
    for i in range(2,int(pow(n,0.5))+1):
        if n%i==0:
            return False
    return True
def d(n):
    s=set()
    for i in range(2,int(pow(n,0.5)+1)):
        if n%i==0 and p(i):
            s|={i}
    return s
f=int(input())
k= list(map(str,d(f)))
if len(k)==0:
    print(f)
else:
    print('*'.join(k))