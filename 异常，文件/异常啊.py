def a(x,y):
    try:
        a=x/y
        print('a=',a)
        return a
    except Exception:
        print('程序出现异常，异常信息：被除数为0')
a(2,0)

