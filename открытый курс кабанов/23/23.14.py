def f(s,e):
    if s>e:return 0
    if s==e: return 1
    else:
        return f(s+1,e)+f(int(bin(s)+'0',2),e)+f(int(bin(s)+'1',2),e)
print(f(int('100',2),int('11101',2)))