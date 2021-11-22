from math import sqrt

class Vetor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'Vetor({self.x}, {self.y})'

    def __abs__(self):
        return sqrt(self.x**2 + self.y**2)

    def __add__(self, vetor):
        return Vetor(self.x + vetor.x, self.y + vetor.y)

    def __iadd__(self, vetor):
        self.x += vetor.x
        self.y += vetor.y
        return self

    def __mul__(self, n):
        return Vetor(self.x * n, self.y * n)

    def __rmul__(self, n):
        return  self * n

if __name__ == '__main__':
    v1 = Vetor(3, 4)
    v2 = Vetor(1, 1)
    print(v1)
    print(abs(v1))
    print(v1 + v2)
    print(v1)
    print(v2)
    print(id(v1))
    v1 += v2
    print(id(v1))
    print(v1)

    print(v1 * 2)
    print(2 * v1)

