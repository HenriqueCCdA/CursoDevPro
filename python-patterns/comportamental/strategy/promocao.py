from abc import ABC, abstractmethod
from decimal import Decimal


class Desconto(ABC):
    '''
    Classe base de todos os descontos
    '''
    @abstractmethod
    def calcular_desconto(self, pedido):
        '''
        Deve calcular o valor de descontos de acordo com o pedido.
        '''

class _DescontoItemRepetido(Desconto):
    '''
    Fornece 10% de desconto em cima de itens com quantidade igual ou superior a 10
    '''
    def calcular_desconto(self, pedido):
        desconto = pedido.soma_dos_itens_com_quantidade_maior_que(10)
        desconto *= Decimal('0.1')
        return pedido.subtotal() - desconto


desconto_item_repetido = _DescontoItemRepetido()