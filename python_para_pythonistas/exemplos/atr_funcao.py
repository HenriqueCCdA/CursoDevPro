nome = 'Renzo'


def f(a: int, b=2, *, c='3') -> str:
    '''
    Funcao exemplo para verifcar atributos
    '''
    print(nome)


f.parametro_dinamico = True

if __name__ == '__main__':
    print(f.__doc__)
    print(f.__defaults__)
    print(f.__globals__)
    print(f.__dict__)
    print(f.__closure__)
    f(1, 5, c=7)
    f(1, b=5, c=7)
    print(f.__kwdefaults__)