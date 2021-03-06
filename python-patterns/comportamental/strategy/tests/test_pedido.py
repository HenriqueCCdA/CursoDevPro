import pytest
from decimal import Decimal

from comportamental.strategy.pedido import Item, Pedido
from comportamental.strategy.promocao import desconto_item_repetido, desconto_grande_pedido


def test_adicionar_item():
    mac=Item('Mac', Decimal('9.32'), 2)
    pedido = Pedido()
    pedido.adicionar(mac)
    assert 1 == len(pedido._itens)

@pytest.mark.parametrize('itens, subtotal',
    [
        (
            [
                Item('Mac', Decimal('9.32'), 2)
            ],
            '18.64'
        ),
        (
            [
                Item('Mac', Decimal('9.32'), 2),
                Item('Galazy', Decimal('1.03'), 3),
            ],
            '21.73'
        )
    ]
)
def test_subtotal(itens, subtotal):
    pedido = Pedido()
    pedido.adicionar(*itens)
    assert Decimal(subtotal) == pedido.subtotal()

@pytest.fixture
def pedido_item_repetido():
    pedido = Pedido()
    pedido.adicionar(Item('Mac', Decimal('100.00'), 10))
    return pedido


def test_total_sem_promocao(pedido_item_repetido):
    assert Decimal('1000.00') == pedido_item_repetido.total()


def test_total_com_desconto_por_item_repetido(pedido_item_repetido):
    assert Decimal('900.00') == pedido_item_repetido.total(desconto_item_repetido)


def test_total_sem_desconto_por_item_repetido():
    pedido = Pedido()
    pedido.adicionar(Item('Mac', Decimal('100.00'), 9))

    assert Decimal('900.00') == pedido.total(desconto_item_repetido)


def test_total_com_desconto_pedido_grande():
    pedido = Pedido()
    pedido.adicionar(Item('Mac', Decimal('1000.00'), 10))

    assert Decimal('9500.00') == pedido.total(desconto_grande_pedido)


def test_total_sem_desconto_pedido_grande():
    pedido = Pedido()
    pedido.adicionar(Item('Mac', Decimal('9999.99'), 1))

    assert Decimal('9999.99') == pedido.total(desconto_grande_pedido)
