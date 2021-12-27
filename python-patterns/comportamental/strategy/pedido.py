from decimal import Decimal

class Item:

    def __init__(self, descricao, preco, quantidade):
        self._descricao = descricao
        self._preco = preco
        self._quantidade = quantidade

    def total(self):
        return self._preco * self._quantidade

class Pedido:
    def __init__(self):
        self._itens = []

    def adicionar(self, *item):
        self._itens.extend(item)

    def subtotal(self):
        return sum(item.total() for item in self._itens)

    def soma_dos_itens_com_quantidade_maior_que(self, limite):
        return sum(item.total() for item in self._itens if item._quantidade >= limite)

    def total(self, promocao=None):
        '''
        Retorna o valor do subtotal depois de aplicado o valor da promação

        :return: Decimal
        '''
        if promocao is None:
            return self.subtotal()

        return promocao.calcular_desconto(self)


class DescontoItemRepetido:
    '''
    Fornece 10% de desconto em cima de itens com quantidade igual ou superior a 10
    '''
    def calcular_desconto(self, pedido):
        desconto = pedido.soma_dos_itens_com_quantidade_maior_que(10) * Decimal('0.1')
        return pedido.subtotal() - desconto
