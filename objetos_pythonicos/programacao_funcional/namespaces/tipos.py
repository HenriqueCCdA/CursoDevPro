a = 5

def f(a=3):
    b = 3
    print(globals())
    print(locals())
    print(a)


class A:
    a = 3
    print(globals())
    a += 3
    print(locals())

#f()