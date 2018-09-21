#函数里面的变量是局部(Local)变量，作用域(Scope)仅在函数内
x = 50

def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)

func(x)
print('x is still',x )