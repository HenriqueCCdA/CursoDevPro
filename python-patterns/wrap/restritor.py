from collections import namedtuple


class EmbrulhoRestritor:
    def __init__(self, embrulhado):
        self._embrulhado = embrulhado

    def __getattr__(self, nome):
        if nome.startswith('_'):
            raise AttributeError(f'Não é possivel acessar atributo protegido: {nome}')
        return getattr(self._embrulhado, nome)


class Cao:
    def __init__(self, nome, raca, sexo):
        self._sexo = sexo
        self.raca = raca
        self.nome = nome

    def latir(self):
        return 'Au'



if __name__ == '__main__':

    rex=Cao('Rex', 'Vira Lata', 'Macho')
    print(rex.nome, rex.raca, rex._sexo)

    rex_restrito=EmbrulhoRestritor(rex)
    print(rex.__dict__)
    print(rex_restrito.latir())
    print(rex_restrito.nome)
    print(rex_restrito._sexo)
