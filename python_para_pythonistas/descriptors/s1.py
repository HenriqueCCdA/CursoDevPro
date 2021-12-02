from pytest import approx

class ItemPedito:
    def __init__(self, descricao, preco, quantidade) -> None:
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade

    def subtotal(self):
        return self.preco * self.quantidade


def test_subtotal():
    item=ItemPedito('Ervilha', 1.21, 2)
    assert approx(2.42, item.subtotal())


def test_subtotal_negativo():
    item=ItemPedito('Ervilha', 1.21, -2)
    assert approx(-2.42, item.subtotal())