for x in range(int(input())):
    k=input()
    if k[:len(k)//2]==k[len(k)//2::]:
        print('YES')
    else:print("NO")