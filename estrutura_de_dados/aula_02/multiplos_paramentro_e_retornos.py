def gerar_ponto():
    return 1, 2, 3

ponto = gerar_ponto()

print(type(ponto))

primeiro, *final = ponto # desmpacotamento

print(primeiro, final)

def argumentos_variaveis(*args):
    print(args)
    print(type(args))


argumentos_variaveis(1, 2)
argumentos_variaveis((1, 2))
argumentos_variaveis(*(1, 2))
argumentos_variaveis(*[1, 2])
argumentos_variaveis(*'ab')

for chave, valor in {'pt': 'Portugues', 'en': 'Ingles'}.items():
    print(chave)
    print(valor)