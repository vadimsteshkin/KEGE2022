l=[]
for i in range(int(input())):
    l.append(list(map(int,input().split())))
def f(l):
    for i in sorted(l,reverse=True):
        if i[1]==1:
            return l.index(i)+1
    return -1
print(f(l))