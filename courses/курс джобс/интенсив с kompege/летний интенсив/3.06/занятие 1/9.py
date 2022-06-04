for _ in range(1,100000):
    k=bin(_)[2::]
    if _%2:
        k='1'+k+'01'
    else:k='10'+k
    if int(k,2)>18:
        print(_)
        break