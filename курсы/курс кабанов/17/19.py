def f(n):
    if n%10==9 and n>0:
        return True
    return False
k=[int(x) for x in open('17_19.txt')]
m=0
q=0
for i in range(len(k)-2):
    if (f(k[i])==False) and (f(k[i+1])==True)  and (f(k[i+2])==False):
        q+=1
        m=max(m,(k[i]+k[i+1]+k[i+2]))
print(q,m)