def fabrica_de_contador():
    contador =0
    def contar():
        nonlocal contador
        contador+=1
        return contador

    return contar

contador_1 = fabrica_de_contador()
contador_2 = fabrica_de_contador()

print(contador_1())
print(contador_1())
print(contador_1())
print(contador_1())

print(contador_2())
print(contador_2())