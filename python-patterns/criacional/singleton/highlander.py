from threading import Lock

class Singleton:
    _instante = None

    def __new__(cls, *args, **kargs):
        with Lock(): # thread safe
            if cls._instante is None:
                cls._instante = super().__new__(cls)
                print('Operacao Cara')
        return cls._instante

    def apaga(self):
        return 'Agapango dados do DB de prod'


class SubSingleton(Singleton):
    def apaga(self):
        return 'Não apagando nada'


if __name__ == '__main__':
    obj1 = Singleton()
    obj2 = SubSingleton()

    print(id(obj1))
    print(id(obj2))

    print(type(obj1))
    print(type(obj2))
