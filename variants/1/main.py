import time
from itertools import *

start = time.time()
f = [''.join(i) for j in range(1, 3) for i in product('0123456789', repeat=j)]
f.append('')


def p(n):
    s = set()
    for i in range(1, int(pow(n, 0.5)) + 1):
        if n % i == 0:
            s |= {i, n // i}
    s = [int(i) for i in s if i % 2 == 0]
    if len(s) > 3:
        return sum(s)
    else:
        return 0


m = []
for i in f:
    for z in f:
        for j in '0123456789':
            k = int('6' + i + '97' + z + '5' + j)
            o = p(k)
            if k > 65000 and o != 0:
                m.append([k, o])
end = time.time()
print(end - start, sorted(m)[:7])
