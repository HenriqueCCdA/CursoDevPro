from collections import deque
from itertools import chain, cycle, zip_longest


def less_to_great_significant_digit_v1(s):
    return map(int, reversed(s))


def less_to_great_significant_digit_v2(s):
    result = []
    s = list(s)
    while s:
        result.append(int(s.pop()))
    return result

def zip_longest_v1(a, b, fillvalue=None):
    a = list(a)
    b = list(b)

    minor, greater = sorted([a, b], key=len)

    minor_with_fillvalues = chain(minor, cycle([fillvalue]))

    return zip(greater, minor_with_fillvalues)


def zip_longest_v2(a, b, fillvalue=None):
    a = list(a)
    b = list(b)

    minor, greater = sorted([a, b], key=len)
    missing = len(greater) - len(minor)
    minor.extend([fillvalue] * missing)
    result = []
    for i, d in enumerate(greater):
        result.append((d, minor[i]))
   
    return result

def binary_sum_v1(n, n2):
    '''
    Resolvendo utilizando a caracteristica do python de ter inteiros de tamanhos "infinitos"
    '''
    n = int(n, 2)
    n2 = int(n2, 2)
    return format(n + n2, 'b')


def binary_sum_v2(n, n2):
    '''
    Resolvendo com zip_longest
    '''
    n = less_to_great_significant_digit_v1(n)
    n2 = less_to_great_significant_digit_v1(n2)
    last_d_sum = 0
    result = deque()
    for d, d2 in zip_longest(n, n2, fillvalue=0):
        d_sum = last_d_sum + d + d2
        last_d_sum = 0 if d_sum < 2 else 1
        result.appendleft(str(d_sum % 2))

    if last_d_sum == 1:
        result.appendleft('1')

    return ''.join(result)


def binary_sum_v3(n, n2):
    '''
    '''
    n = less_to_great_significant_digit_v1(n)
    n2 = less_to_great_significant_digit_v1(n2)
    last_d_sum = 0
    result = deque()
    for d, d2 in zip_longest_v1(n, n2, fillvalue=0):
        d_sum = last_d_sum + d + d2
        last_d_sum = 0 if d_sum < 2 else 1
        result.appendleft(str(d_sum % 2))

    if last_d_sum == 1:
        result.appendleft('1')

    return ''.join(result)


def binary_sum_v4(n, n2):
    '''
    '''
    n = less_to_great_significant_digit_v2(n)
    n2 = less_to_great_significant_digit_v2(n2)
    last_d_sum = 0
    result = deque()
    for d, d2 in zip_longest_v2(n, n2, fillvalue=0):
        d_sum = last_d_sum + d + d2
        last_d_sum = 0 if d_sum < 2 else 1
        result.appendleft(str(d_sum % 2))

    if last_d_sum == 1:
        result.appendleft('1')

    return ''.join(result)

print(binary_sum_v1('111110', '1100')) # 1001010.
print(binary_sum_v2('111110', '1100')) # 1001010.
print(binary_sum_v3('111110', '1100')) # 1001010.
print(binary_sum_v4('111110', '1100')) # 1001010.
