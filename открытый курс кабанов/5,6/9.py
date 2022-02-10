for _ in range(1000,10000):
    k=str(_)
    o=int(k[0])*int(k[1])
    o1=int(k[2])*int(k[3])
    if str(min(o,o1))+str(max(o,o1))=='1214':
        print(_)