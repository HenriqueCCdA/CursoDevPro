from comportamental.strategy_pythonico.promocao import desconto_null_object


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

    def total(self, promocao=desconto_null_object):
        '''
        Retorna o valor do subtotal depois de aplicado o valor da promação

        :return: Decimal
        '''
        return promocao(self)
