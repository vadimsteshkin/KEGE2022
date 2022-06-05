for _ in range(9999):
    k=bin(_)[2::]
    s=sum([int(i) for i in k])
    if s%2:k+='11'
    else:k='11'+k
    if int(k,2)>102:
        print(_)
        break