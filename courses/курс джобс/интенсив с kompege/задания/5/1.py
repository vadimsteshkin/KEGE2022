for _ in range(77):
    k=bin(_)[2::]
    for i in range(2):
        k+=str(sum([int(i) for i in k])%2)
    if int(k,2)>77:
        print(_)
        break