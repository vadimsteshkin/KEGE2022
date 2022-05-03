# Найдите все натуральные числа, принадлежащие отрезку [101 000 000; 102 000 000], у которых ровно три различных чётных делителя.
# В ответе перечислите найденные числа в порядке возрастания.
from functools import *
@lru_cache()
def d(n):
    s=set()
    for i in range(1,int(pow(n,0.5))+1):
        if n%i==0:
            s|={i,n//i}
    return sorted(s)
for i in range(101000000, 102000000):
    m=[x for x in d(i) if x%2==0]
    if len(m)==3:
        print(i)