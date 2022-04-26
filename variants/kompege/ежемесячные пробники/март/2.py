for x in range(2):
    for y in range(2):
        for z in range(2):
            if (y<=z) and (not(z and x)):
                print(z,x,y)