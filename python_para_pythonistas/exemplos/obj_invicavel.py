class Invocavel:

    def __init__(self, numero):
        self.numero = numero

    def __call__(self):
        return self.numero

if __name__ == '__main__':
    invocaveis = (Invocavel(i) for i in range(1, 3))

    for invovavel in invocaveis:
        print(invovavel())