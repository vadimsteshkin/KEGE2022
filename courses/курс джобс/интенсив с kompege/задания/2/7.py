for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not(((not(x)) or y or (not(z))) and(x or(not(y))) or (not(w))):
                    print(x,z,w,y)