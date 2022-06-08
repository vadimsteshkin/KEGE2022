for a in range(10):
    for b in range(10):
        # x = int(f'12345{a}7{b}8')
        x = 12345*10000 + a*1000 + 7*100 + b*10 + 8
        if x % 23 == 0:
            print(x, x // 23)