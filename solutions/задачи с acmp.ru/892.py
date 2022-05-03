k=int(input())
if k in range(3,6):
    print('Spring')
elif k in range(6,9):
    print('Summer')
elif k in range(9,12):
    print('Autumn')
elif k in range(1,3) or k==12:
    print('Winter')
else:
    print('Error')