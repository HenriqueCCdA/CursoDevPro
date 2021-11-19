class Arvore:
    '''
        >>> for noh in Arvore(0, Arvore(-2, Arvore(-4), Arvore(-1)), Arvore(10))
        ...     print(noh)
        -4
        -1
        -2
         0
        10
    '''

    def __init__(self, valor, esquerda=None, direita=None):
        self.esquerda = esquerda
        self.direita = direita



#               0
#      -2             10
#   -4    -1
