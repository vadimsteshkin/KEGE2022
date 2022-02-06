def nod(a,b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
 
    return a + b
print(nod(234,10))
#нахождение НОК A*B/NOK(A,B)