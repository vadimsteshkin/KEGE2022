for _ in range(999):
    k=bin(_)[2::]
    if _%2:k+='10'
    else:k+='01'
    if int(k,2)>81:
        print(int(k,2))
        break