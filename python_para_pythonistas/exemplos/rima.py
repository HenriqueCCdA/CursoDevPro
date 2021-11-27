frutas = 'banana castanha pequi caju umbu caqui amora'.split()

if __name__ == '__main__':
    print(sorted(frutas, key=lambda fruta: fruta[::-1]))
    print(frutas)