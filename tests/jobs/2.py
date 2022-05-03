for x in range(2):
    for w in range(2):
        for y in range(2):
            for z in range(2):
                if not((y or x)==((y<=w) or (not(z)))):
                    print(z,w,y,x)
print(19//20)