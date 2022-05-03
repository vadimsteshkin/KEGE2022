lst=[]
for i in range(int(input())):
    lst.append(int(input()))
print(lst.count(min(lst)))