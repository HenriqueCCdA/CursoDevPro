from collections import namedtuple


Item=namedtuple('Item', 'descricao preco quantidade')

class Pedido:
    def __init__(self):
        self._itens = []

    def adicionar(self, item):
        self._itens.append(item)