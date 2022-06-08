f = open('26_7.txt')
a = [0] * 2_000_001
n = int(f.readline())
for i in range(n):
    m, e = map(int, f.readline().split())
    a[m] += 1
    a[e] -= 1
mx = 0
k, c = 0, 0
st, en = -1, 0
for i in range(2_000_001):
    k0 = k
    k += a[i]
    if k >0 and st == -1:
        st = i
    if k == 0 and k0 > 0:
        en = i
        c += 1
        mx += (en - st)
        st, en = -1, 0
print(c, mx)
