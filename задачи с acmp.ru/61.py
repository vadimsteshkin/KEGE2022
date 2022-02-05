o, p = 0, 0
for i in range(4):
    k = input().split()
    o += int(k[0])
    p += int(k[1])
if o > p:
    print('1')
if o == p:
    print('DRAW')
if o<p:
    print('2')
