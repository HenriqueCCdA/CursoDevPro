class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __repr__(self):
        return f'Carta(valor={self.valor}, naipe={self.naipe})'

if __name__ == '__main__':
    print(Carta('A', '♣️'))