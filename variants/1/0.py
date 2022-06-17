a = [[0 for j in range(10)] for i in range(100)]
for i in a:
    if a.index(i)==98:
        i[0] = 12
    print(*i)
