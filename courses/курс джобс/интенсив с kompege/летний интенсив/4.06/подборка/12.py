from itertools import *

m = []


def f(x, s, e):
    p = 10 <= x <= 25
    q = 15 <= x <= 30
    r = 25 <= x <= 40
    a = s <= x <= e
    return (q <= (not (r))) and a and (not (p))


ox = [i / 4 for i in range(41 * 4)]
for w, e in combinations(ox, 2):
    if all(f(x, w, e)==0 for x in ox):
        m.append(abs(w - e))
print(max(m))
