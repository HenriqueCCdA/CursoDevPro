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

    def total(self):
        return sum(item.total() for item in self._itens)