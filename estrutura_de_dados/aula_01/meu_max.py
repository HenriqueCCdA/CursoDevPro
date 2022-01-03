from math import inf
from time import time


def meu_max(iteravel):
    '''
    Análise do algoritmo
    Tempo de execução, algoritmo O(n)
    Em memória O(1)
    '''
    numero_max = -inf
    for numero in iteravel:
        if numero > numero_max:
            numero_max = numero

    return numero_max

if __name__ == '__main__':
    print(meu_max([1]))
    print(meu_max([1, 100]))

    print('Estudo Experimental sobre o tempo de execução da função max')

    inicio = 1_000_000
    for n in range(inicio, inicio * 20 + 1, inicio):
        input = range(n)
        inicio = time()
        meu_max(input)
        fim = time()
        tempo_de_execucao_em_segundos = fim - inicio
        print('*' * int(tempo_de_execucao_em_segundos * 10), n)