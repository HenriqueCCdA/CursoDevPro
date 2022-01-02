from abc import ABC, abstractmethod
from decimal import Decimal


def desconto_null_object(pedido):
    return pedido.subtotal()


def desconto_item_repetido(pedido):
    desconto = pedido.soma_dos_itens_com_quantidade_maior_que(10)
    desconto *= Decimal('0.10')
    return pedido.subtotal() - desconto


def desconto_grande_pedido(pedido):
    subtotal = pedido.subtotal()
    if subtotal < 10000:
        return subtotal

    return pedido.subtotal() * Decimal('0.95')


todos_descontos=[desconto_item_repetido, desconto_grande_pedido]

def melhor_promocao(pedido):
    return min(desconto(pedido) for desconto in todos_descontos)