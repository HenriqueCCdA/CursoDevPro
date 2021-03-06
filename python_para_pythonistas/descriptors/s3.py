from pytest import approx, raises


class Quantidade:

    def  __init__(self, nome):
        self._nome=f'_{nome}'

    def __get__(self, item, owner):
        return getattr(item, self._nome)

    def __set__(self, item, valor):
        if valor <= 0:
            raise TypeError('Quantidade deveria ser positiva')
        setattr(item, self._nome, valor)


class ItemPedito:

    quantidade = Quantidade('quantidade')
    preco = Quantidade('preco')

    def __init__(self, descricao, preco, quantidade) -> None:
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade


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


def test_propriedade_de_descriptor():
    item=ItemPedito('Ervilha', 1.21, 2)
    assert {'descricao':'Ervilha', '_preco' : 1.21, '_quantidade': 2} == item.__dict__
