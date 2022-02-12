for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                if ((not(a) and not(b))or (b==c) and d) ==0:
                    print(c,a,d,b)