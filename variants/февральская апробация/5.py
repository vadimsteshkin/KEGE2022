for _ in range(10000):
    b=bin(_)[2::]
    if _%2==0:b+=bin(sum([int(i) for i in b]))[2::]
    else:
        b='1'+b+'00'
    if int(b,2)>215:
        print(_)
        break