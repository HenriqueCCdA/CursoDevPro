from time import strftime
from functools import partial, wraps


# def logar(fmt='%H:%M:%S'):
#     if callable(fmt):
#         func=fmt
#         aux_decorator = logar
#         return aux_decorator()(func)

#     def decorador(func):
#         @functools.wraps(func)
#         def envoltoria(*args, **kwargs):
#             agora = strftime(fmt)
#             print(f'{agora} executada função {func.__name__}')
#             return func(*args, **kwargs)
#         return envoltoria
#     return decorador

def logar(func=None, *, fmt='%H:%M:%S'):
    if func is None:
        return partial(logar, fmt=fmt)
        # def decorator(func):
        #     return logar(func, fmt=fmt)
        # return decorator

    @wraps(func)
    def envoltoria(*args, **kwargs):
        agora = strftime(fmt)
        print(f'{agora} executada função {func.__name__}')
        return func(*args, **kwargs)
    return envoltoria

# class logar:
#     def __init__(self, fmt='%H-%M-%S'):
#         self.fmt = fmt

#     def __call__(self, func):
#         @functools.wraps(func)
#         def envoltoria(*args, **kwargs):
#             agora = strftime(self.fmt)
#             print(f'{agora} executada função {func.__name__}')
#             return func(*args, **kwargs)
#         return envoltoria


@logar
def ola_mundo():
    '''Função Olá mundo'''
    return 'Olá Mundo'


@logar()
def hello_world():
    '''Função Hello Word'''
    return 'Hello world'

@logar(fmt='%H-%M-%S')
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