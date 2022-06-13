p='777999'
print(max(sorted(p)[::-1],key=lambda x:p.count(x)))
