from inspect import getfullargspec
from time import sleep, strftime
from functools import wraps
from decorator import decorator

def logar(f):
    def executar_com_tempo(*args, **kwargs):
        print(strftime('%H:%M:%S'))
        return f(*args, **kwargs)

    return executar_com_tempo


def logar2(f):
    @wraps(f)
    def executar_com_tempo(*args, **kwargs):
        print(strftime('%H:%M:%S'))
        return f(*args, **kwargs)

    return executar_com_tempo


def logar3(fmt):
    def decorator(f):
        @wraps(f)
        def executar_com_tempo(*args, **kwargs):
            print(strftime(fmt))
            return f(*args, **kwargs)

        return executar_com_tempo
    
    return decorator


def logar4(fn=None, *, fmt='%H:%M:%S'):
    if fn is not None:
        return logar4(fmt=fmt)(fn)

    def decorator(f):
        @wraps(f)
        def executar_com_tempo(*args, **kwargs):
            print(strftime(fmt))
            return f(*args, **kwargs)

        return executar_com_tempo
    
    return decorator

@decorator
def logar5(f, fmt='%H:%M:%S', *args, **kwargs):
    print(strftime(fmt))
    return f(*args, **kwargs)

@logar5
def mochileiro():   
    return 42

@logar5(fmt='%d/%m/%Y %H:%M:%S')
def ola(nome):
    return f'Ola {nome}'


if __name__ == '__main__':
    print(getfullargspec(mochileiro))
    print(getfullargspec(ola))
    print(mochileiro())
    print('nome func:', mochileiro.__name__)
    print(ola('Renzo'))
    print('nome func:', ola.__name__)
    sleep(1)
    print(mochileiro())
    print(ola('Luciano'))

