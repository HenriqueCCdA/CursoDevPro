import operator
import pytest
import functools

def divisao_por_2_v1(n):
    return n // 2

def divisao_por_2_v2(n):
    return operator.floordiv(n, 2)

def criador_de_divisao(funcao, quociente):
    def f(n):
        return funcao(n, quociente)

    return f

divisao_por_2_v3 = criador_de_divisao(operator.floordiv, 2)

def f(a, b):
    return a, b


@pytest.mark.parametrize('funcao', [
    divisao_por_2_v1,
    divisao_por_2_v2,
    divisao_por_2_v3,
])
def test_divisao(funcao):
    assert 5 == funcao(10)


def test_partial_manual():
    def criador_de_atalho(funcao, primeiro):
        def g(*args):
            return funcao(primeiro, *args)
        return g

    atalho = criador_de_atalho(f, 1)

    assert (1, 2) == atalho(2)
    assert (1, 3) == atalho(3)
    assert (1, 4) == atalho(4)


def test_partial_functools():

    atalho = functools.partial(f, 1)

    assert (1, 2) == atalho(2)
    assert (1, 3) == atalho(3)
    assert (1, 4) == atalho(4)



def test_partial_functools_2_param():

    atalho = functools.partial(f, 1, b=2)

    assert (1, 2) == atalho()
