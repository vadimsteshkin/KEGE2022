k = open('26_1.txt').readlines()
k1 = int(k[0].split()[0])
l = sorted(list(map(int, k[1::])))
m = 0
k = -1
ch = 0
n = 0
while m < k1:
    if ch % 2 == 0:
        m += l[k]
        print(l[k])
        k -= 1
    else:
        m += l[n]
        print(l[n])
        n += 1

    ch += 1
print(ch - 1, )
