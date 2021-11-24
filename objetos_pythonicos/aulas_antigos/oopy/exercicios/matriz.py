from itertools import product

def gerar_linha(matriz, n):
    return matriz[n]

def gerar_coluna(matriz, n):
    return [ linha[n] for linha in matriz]


class Matriz:

    def __init__(self, lista) -> None:
        self.lista = lista

    def __matmul__(self, other) -> None:
        m1, m2=self.lista, other.lista
        n_lin, n_col = len(m1), len(m2[0])
        resultado=[ [0 for _ in range(n_col) ] for _ in range(n_lin)]

        for i, j in product(range(n_lin), range(n_col)):
            for ele_linha, ele_coluna in zip(gerar_linha(m1, i), gerar_coluna(m2, j)):
                resultado[i][j] += ele_linha * ele_coluna

        return Matriz(resultado)

    def __repr__(self):
        return f'Matriz({self.lista})'