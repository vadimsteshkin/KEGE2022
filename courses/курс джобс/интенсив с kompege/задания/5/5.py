for _ in range(9999):
    k=bin(_)[2::]
    k+=k[-1]
    if k.count('1')%2:k+='10'
    else:k+='00'
    if int(k,2)>97:
        print(_)