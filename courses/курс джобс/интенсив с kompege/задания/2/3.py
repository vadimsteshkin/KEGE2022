for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not((not(x)) and (not(y)) or(x==z) or w):
                    print(z,y,x,w)