for a in range(2,1000000):
    for x in range(1,10000):
        if all(((x&a!=0)<=(((x&17==0) and (x&5==0))<=(x&3!=0)))):
            print(a)