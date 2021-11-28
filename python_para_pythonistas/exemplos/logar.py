from time import strftime
import functools


def logar(func):
    def envoltoria():
        agora = strftime('%H:%M:%S')
        print(f'{agora} executada função {func.__name__}')
        return func()
    envoltoria.__name__ = func.__name__
    envoltoria.__doc__ = func.__doc__
    return envoltoria


def logar2(func):
    @functools.wraps(func)
    def envoltoria():
        agora = strftime('%H:%M:%S')
        print(f'{agora} executada função {func.__name__}')
        return func()
    envoltoria.__name__ = func.__name__
    envoltoria.__doc__ = func.__doc__
    return envoltoria


def logar3(func):
    @functools.wraps(func)
    def envoltoria(*args, **kwargs):
        agora = strftime('%H:%M:%S')
        print(f'{agora} executada função {func.__name__}')
        return func(*args, **kwargs)
    return envoltoria


def logar4(fmt):
    def decorador(func):
        @functools.wraps(func)
        def envoltoria(*args, **kwargs):
            agora = strftime(fmt)
            print(f'{agora} executada função {func.__name__}')
            return func(*args, **kwargs)
        return envoltoria
    return decorador

class logar5:
    def __init__(self, fmt):
        self.fmt = fmt

    def __call__(self, func):
        @functools.wraps(func)
        def envoltoria(*args, **kwargs):
            agora = strftime(self.fmt)
            print(f'{agora} executada função {func.__name__}')
            return func(*args, **kwargs)
        return envoltoria


def ola_mundo():
    '''Função Olá mundo'''
    return 'Olá Mundo'

# ola_mundo = logar2(ola_mundo)

decorador = logar4('%H-%M-%S')
ola_mundo = decorador(ola_mundo)

# @logar2
# def hello_world():
#     '''Função Hello Word'''
#     return 'Hello world'

@logar4('%H-%M-%S')
def hello_world():
    '''Função Hello Word'''
    return 'Hello world'

@logar5('%H-%M-%S')
def hello(nome):
    '''Função hello'''
    return f'Hello {nome}'


if __name__ == '__main__':
    print(ola_mundo())
    print(ola_mundo.__name__)
    print(ola_mundo.__doc__)
    print(hello_world())
    print(hello_world.__name__)
    print(hello_world.__doc__)

    print(hello('Matheus'))
    print(hello.__name__)
    print(hello.__doc__)