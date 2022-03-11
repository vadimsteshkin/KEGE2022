input()
def c(k):
    for i in k:
        if i <438:return 'Crash', k.index(i)+1
    return 'No crash',''
print(*c(list(map(int,input().split()))))