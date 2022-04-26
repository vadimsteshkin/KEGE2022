for a in range(1,1000):
    for x in range(1,1000):
        for y in range(1,1000):
            if all((5*x+3*y!=60) or((a>x)and(a>y)))