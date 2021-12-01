def criar_conta(saldo):
    def retirar(valor):
        nonlocal saldo
        if valor >= saldo:
            raise ValueError('Valor não pode ser maior que saldo')
        saldo-=valor
        return saldo

    def depositar(valor):
        nonlocal saldo
        saldo += valor
        return saldo

    return retirar, depositar


if __name__ == '__main__':
    retirar, depositar =criar_conta(400)
    print(retirar(250))
    print(depositar(250))
    print(retirar(300))
