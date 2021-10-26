def  hanoi_rec(n, orig='A', aux='B', dest='C'):
    '''
    Solução recursiva de Torre de hanoi

    t(n) = 1 + 2 x t(n-1)
    t(n) = 1 + 2 x (1 + 2 x t(n-2) ) = 1 + 2 + 4 x t(n-2)
    t(n) = 1 + 2 + 4 x ( 1 + 2 x t(n-3) ) = 1 + 2 + 4 + 8 x t(n-3)
    t(n) = 1 + 2 + 4 + 8 + ... + 2^n x t(0)
    
    2 x t(n) = 2 + 4 + 16 + ... + 2^(n+1) x t(0)
       - t(n) = 1 + 2 + 4 + 8 + ... + 2^n x t(0)
    _____________________________________________
    t(n) = 2^(n+1) - 1 => O(2^n)

    m(n) = 1 + m(n-1) - 1 + m(1) => O(n)

    '''

    if n>=1:
        hanoi_rec(n-1, orig, dest, aux)
        print(f'disco {n}:{orig} -> {dest}')
        hanoi_rec(n-1, aux, orig, dest)


def  hanoi_it(n, orig='A', aux='B', dest='C'):
    '''
    Solução recursiva de Torre de hanoi

    t(n) = 1 + 2 x t(n-1)
    t(n) = 1 + 2 x (1 + 2 x t(n-2) ) = 1 + 2 + 4 x t(n-2)
    t(n) = 1 + 2 + 4 x ( 1 + 2 x t(n-3) ) = 1 + 2 + 4 + 8 x t(n-3)
    t(n) = 1 + 2 + 4 + 8 + ... + 2^n x t(0)
    
    2 x t(n) = 2 + 4 + 16 + ... + 2^(n+1) x t(0)
       - t(n) = 1 + 2 + 4 + 8 + ... + 2^n x t(0)
    _____________________________________________
    t(n) = 2^(n+1) - 1 => O(2^n)

    m(n) = 1 + m(n-1) - 1 + m(1) => O(n)

    '''

    stack=[(False, n, orig, aux, dest)]

    while stack:
        print_flag, n, orig, aux, dest = stack.pop()
        if n < 1:
            continue
        if not print_flag:
            stack.append((True, n, orig, aux, dest)) 
            stack.append((False, n - 1, orig, dest, aux))
        else:
            print(f'disco {n}:{orig} -> {dest}') 
            stack.append((False, n - 1, aux, orig, dest))



for i in range(1, 4):
    print(f'######## Hanoi_rec {i}')
    hanoi_rec(i)

for i in range(1, 4):
    print(f'######## Hanoi_it {i}')
    hanoi_it(i)
