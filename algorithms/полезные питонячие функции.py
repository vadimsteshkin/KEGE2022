#lambada func
k=lambda x,y: x**y
print(k(10,2)) #создает функцию
#filter
k=[1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
get=lambda x: x%2==0
print(list(filter(get,k)))
#reduce