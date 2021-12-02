from pytest import approx, raises

class ItemPedito:
    def __init__(self, descricao, preco, quantidade) -> None:
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, valor):
        if valor <= 0:
            raise TypeError('Quantidade deveria ser positiva')
        self._quantidade = valor

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if valor <= 0:
            raise TypeError('Preço deveria ser positiva')
        self._preco = valor



    def subtotal(self):
        return self.preco * self.quantidade


def test_subtotal():
    item=ItemPedito('Ervilha', 1.21, 2)
    assert approx(2.42, item.subtotal())


def test_set_quantidade_negativa():
    item=ItemPedito('Ervilha', 1.21, 2)
    with raises(TypeError):
        item.quantidade = -2
    assert approx(-2.42, item.subtotal())


def test_set_quantidade_negativa_no_init():
    with raises(TypeError):
        item=ItemPedito('Ervilha', 1.21, -2)


def test_set_preco_negativa():
    item=ItemPedito('Ervilha', 1.21, 2)
    with raises(TypeError):
        item.preco = -1.21
    assert approx(-2.42, item.subtotal())


def test_set_preco_negativa_no_init():
    with raises(TypeError):
        item=ItemPedito('Ervilha', -1.21, 2)
