for _ in range(1000000):
    k=bin(_)[2::]
    if _%2:
        k='1'+k+'01'
    else:
        k+='10'
    if int(k,2)>441:
        print(_)
        break