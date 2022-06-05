for _ in range(1,9999):
    k=bin(_)[2::]
    if _%2:k='1'+k+'1'
    else:k=k+k[-2]+k[-1]
    if int(k,2)>100:
        print(_)
        break