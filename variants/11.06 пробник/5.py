for _ in range(10000):
    k=bin(_)[2::]
    if _%2:
        k='1'+k+'00'
    else:k='10'+k+'10'
    if int(k,2)>100:
        print(int(k,2))