s = [int(i) for i in open('107_17.txt')]
k = min([i for i in s if i % 21 == 0])
q = 0
m = 0
for i in range(len(s) - 1):
    if (s[i] % k)==0 or (s[i + 1] % k) == 0:
        q += 1
        m = max(m, s[i] + s[i + 1])
print(q, m)
