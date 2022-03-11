for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if ((w<=y) or (not(y<=z))) and(not(x)) and (not(x==z)):
                    print(w,x,z,y)