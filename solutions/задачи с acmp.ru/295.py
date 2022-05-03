def f (s,t):
    for i in t:
        if t.count(i)>s.count(i):
            return 'IMPOSSIBLE'
    return t
m=input()
k=input()
print(f(m,k))