def prime(n):
    s=set()
    for i in range(2,int(pow(n,0.5))):# чтобы проверить число на простоту,нужно перебрать делители до корня
        if n%i==0:
            return False
    return True
print(prime(int(input())))#возвращает True если простое