from itertools import cycle
from time import perf_counter_ns

lista_de_numeros=list(range(10))

print(id(lista_de_numeros))
print(id(lista_de_numeros[0]))
print(id(lista_de_numeros[1]))
print(id(lista_de_numeros[2]))

lista_de_numeros.append(10)

maior_delta = 0
counter=0
for i in cycle((11, 12)):
    inicio = perf_counter_ns()
    lista_de_numeros.append(i)
    delta = perf_counter_ns() - inicio
    counter+= 1
    if delta > maior_delta:
        maior_delta = delta
        print(maior_delta, counter)
        counter=0
