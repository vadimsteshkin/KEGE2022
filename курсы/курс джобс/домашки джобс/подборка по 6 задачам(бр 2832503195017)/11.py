for i in range(36):
    k=81**20-9**i+50
    q=0
    while k>0:
        q+=k%9
        k//=9
    if q==138:
        print(i)