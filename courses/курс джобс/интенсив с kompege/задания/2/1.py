for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                if not((not(a)) and (not(b)) or(c==b) or d):
                    print(c,d,b,a)