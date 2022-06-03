for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (w or y) and (x<=z) and (not(w)):
                    print(y,z,w,x)