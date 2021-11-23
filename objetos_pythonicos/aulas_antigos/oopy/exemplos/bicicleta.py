import abc

class Bicicleta(abc.ABC):
    _marca = 'Caloi'

    def __init__(self):
        self._velocidade = 0

    @classmethod
    def marca(cls):
        return cls._marca

    @staticmethod
    def rodas():
        return 2

    @property
    def velocidade(self):
        return self._velocidade

    @velocidade.setter
    def velocidade(self, valor):
        if valor >= 0:
            self._velocidade= valor
        else:
            self._velocidade= 0

    @abc.abstractmethod
    def pedalar(self):
       pass

    @abc.abstractmethod
    def frear(self):
        pass

class Monark(Bicicleta):
    _marca = 'Monark'

    # def pedelar(self):
    #     self.velocidade+=10

    # def frear(self):
    #     self.velocidade-=3
    #     if self.velocidade < 0:
    #         self.velocidade = 0


if __name__ == '__main__':
    bicicleta = Monark()
    print(Bicicleta.marca())
    # bicicleta.pedelar()
    # bicicleta.frear()
    # bicicleta.frear()
    # bicicleta.frear()
    # bicicleta.frear()
    bicicleta.velocidade = -4
    print(bicicleta.velocidade)
    print(Monark.marca())
    print(Monark.rodas())