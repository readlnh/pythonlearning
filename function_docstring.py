def print_max(x, y):
    '''打印两个数中比较大的那一个

    两个数应该都是整数'''
    x = int(x)
    y = int(y)

    if x > y:
        print(x)
    elif x == y:
        print('x equal y')
    else:
        print(y)

print_max(3, 5)
print(print_max.__doc__)