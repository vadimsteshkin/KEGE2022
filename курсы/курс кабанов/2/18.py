for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if (((z<=x) and (x<=w)) or (y==(x or z)))==0:
                    print(y,x,w,z)