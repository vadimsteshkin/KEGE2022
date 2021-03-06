# Автомат обрабатывает десятичное натуральное число N по следующему алгоритму:
# 1) Строится двоичная запись числа N.
# 2) К этой записи дописываются справа ещё два разряда по следующему правилу: если N чётное, в конец числа (справа) приписывается 1, в противном случае справа приписывается 0.
# 3) Пункт 2 повторяется ещё один раз.
# Например, двоичная запись 1001 числа 9 будет преобразована в 100101. Полученная таким образом запись (в ней на два разряда больше, чем в записи исходного числа N) является двоичной записью числа – результата работы данного алгоритма.
# Укажите максимальное число N, для которого результат работы алгоритма будет меньше 171. В ответе это число запишите в десятичной системе счисления.
def f(n):
    k=bin(n)[2::]
    if n%2==0:
        k+='10'
    else:k+='01'
    return int(k,2)
for i in range(1000):
    if f(i)<171:
        print(i)
#42