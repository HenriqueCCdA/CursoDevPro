from pytest import approx, raises
from framework import Propriedade, Modelo


class Quantidade(Propriedade):
    def validar(self, valor):
        if valor <= 0:
            raise TypeError('Quantidade deveria ser positiva')


class ItemPedito(Modelo):

    quantidade = Quantidade()
    preco = Quantidade()

    def __init__(self, descricao, preco, quantidade):
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