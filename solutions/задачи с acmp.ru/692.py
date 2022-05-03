def b(k):
    for i in range(20):
        if 2**i==k:
            return 'YES'
    return 'NO'
print(b(int(input())))