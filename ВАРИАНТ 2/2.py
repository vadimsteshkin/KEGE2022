for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (x or (not(z) and y) and not(w))==0:
                    print(x,y,z,w)