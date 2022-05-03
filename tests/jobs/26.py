f = open("26.txt")
l = []
q = 0
for i in range(10001):
    l.append([0 for j in range(10001)])
for i in range(int(f.readline())):
    x, y = map(int, f.readline().split())
    l[x][y] = 1
for i in l:
    m = 0
    lst = []
    for j in i:
        if j == 1:
            lst.append(i.index(j))
            print(lst,i)
    for k in range(len(lst) - 1):
        q += ((lst[k] - lst[k + 1]) // 20)
        m += 1
    l[l.index(i)][0] = m
m = max([i[-1] for i in l])
print(q, m)
