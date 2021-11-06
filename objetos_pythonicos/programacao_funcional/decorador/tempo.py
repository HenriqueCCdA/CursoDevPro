from time import sleep, strftime
from functools import wraps

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


@logar2
def mochileiro():   
    return 42

@logar2
def ola(nome):
    return f'Ola {nome}'


if __name__ == '__main__':
    print(mochileiro())
    print('nome func:', mochileiro.__name__)
    print(ola('Renzo'))
    print('nome func:', ola.__name__)
    sleep(1)
    print(mochileiro())
    print(ola('Luciano'))

