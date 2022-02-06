# Рассмотрим произвольное натуральное число, представим его всеми возможными способами в виде произведения двух натуральных чисел и найдём для каждого такого произведения разность сомножителей.
#
# Например, для числа 16 получим: 16 = 16*1 = 8*2 = 4*4, множество разностей содержит числа 15, 6 и 0. Найдите все натуральные числа, принадлежащие отрезку [1 000 000; 2 000 000],
# у которых составленное описанным способом множество разностей будет содержать не меньше трёх элементов, не превышающих 100.
# В ответе перечислите найденные числа в порядке возрастания.

def f(n):
    s=list()
    for i in range(1,int(pow(n,0.5)+1)):
        if n%i==0:
            s.append(abs((n//i)-i))
    return s
for i in range(10**6,2*10**6+1):
    m=f(i)
    if len(m)>2 and max(m)<100:
        print(i,m)