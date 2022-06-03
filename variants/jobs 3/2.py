for x in range(2):
    for y in range(2):
        for z in range(2):
            if (not(x) and y and z) or(not(x and(not (z)))):
                print(y,z,x)