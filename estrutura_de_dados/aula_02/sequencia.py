# Sequencia Mutável:

lista = list()

print(id(lista))
print(lista)

lista.append(1)

print(id(lista))
print(lista)

print('### Soma de lista')
lista = lista + [1]
print(id(lista))
print(lista)

# Sequencias Imutáveis:

tupla = (1, 3)

print(type(tupla))
print(id(tupla))

print('### Soma de tupla')
tupla += (2, 4)
print(id(tupla))
print(tupla)

print('### Soma de String')

a='Renzo'
print(id(a))

a+='Nuccitelli'
print(id(a))

print('### Objeto imatável mutante')

tupla =(lista, )

print(tupla)
print(id(tupla[0]))
lista.append(6)
print(tupla)
print(id(tupla[0]))
