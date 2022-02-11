n = 600000
a = []
for i in range(n + 1):
    a.append(i)
a[1] = 0
i = 2
while i <= n:
    if a[i] != 0:
        j = i + i
        while j <= n:
            a[j] = 0
            j = j + i
    i += 1
a = set(a)
a.remove(0)
def f(n):
    global a
    s=set()
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            s|={i,n//i}
    m=set()
    for k in s:
        if k in a:
            m.add(k)
    return sum(m)
print(f(10))
for i in range(660000,99999999):
    m=f(i)
    if m%10==5:
        print(i,m)