# f=open('9.txt').readlines()
# o=0
# for i in range(len(f)):
#     k=sorted(list(map(int,f[i].split('\t'))))
#     if k[2]<(k[1]+k[0]):
#         o+=1
# print(o)



# def f(s,e):
#     if s>e:return 0
#     if s==e:return 1
#     else:
#         if s%2==0:
#             return f(s+1,e)+f(s*2,e)+f(s+1,s)
#         else:return f(s+1,e)+f(s*2,e)+f(s+2,s)
# print(f(3,9)*f(9,17)*f(17,25))


#
# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [2422000; 2422080],
# простые числа. Выведите все найденные простые числа в порядке возрастания, слева от каждого числа выведите его номер по порядку.
#
# P.S. Программа должна вывести 4 числа, в ответе укажите наибольшее.

# def d(n):
#     for i in (2,n):
#         if n%i==0:return 0
#     return 1
# print(d(15))
# for i in range(2422000, 2422080):
#     if d(i)==1:
#         print(i)



# (4x + 3y < A) ∨ (x ≥ y) ∨ (y ≥ 13)
for a in range(1000):
    for x in range(1000):
        for y in range(1000):
            if all(((4*x+3*y)<a) or (x>=y) or (y>=13)):
                print(a)