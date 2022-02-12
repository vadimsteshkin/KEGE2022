for i in range(2,3600):
    if int('10',7)<=i<int('1000',7) and int('100',6)<=i<int('1000',6) and i%13==3:
        print(i)
        break