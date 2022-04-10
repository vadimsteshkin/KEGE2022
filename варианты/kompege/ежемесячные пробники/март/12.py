for _ in range(301,1000):
    k='5'*_
    while '55555' in k:
        k=k.replace('55555','88',1)
        k=k.replace('888','55',1)
    print(k.count('5'),_)