from decimal import Decimal

from comportamental.strategy.pedido import Item, Pedido


def test_adicionar_item():
    mac=Item('Mac', Decimal('9.32'), 1)
    pedido = Pedido()
    pedido.adicionar(mac)
    assert 1 == len(pedido._itens)