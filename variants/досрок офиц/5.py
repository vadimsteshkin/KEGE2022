for _ in range(10000):
    k=bin(_)[2::]
    if _%2==0:k='10'+k
    else:k='1'+k+'01'
    if int(k,2)>441:
        print(_)
        break