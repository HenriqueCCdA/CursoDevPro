from random import shuffle


def max_min_ord(lst):
    """
    Calculate the maximum and minimum of a list lst (lista ordenada)
    :param: lst: list
    :return: tuple: (max, min)
    """
    if len(lst) == 0:
        raise Exception('Lista vazia')

    return lst[-1], lst[0], # O(1) 


def max_min(lst):
    """
    Calculate the maximum and minimum of a list lst (lista nao ordenada)
    :param: lst: list
    :return: tuple: (max, min)
    """
    if len(lst) == 0:
        raise Exception('Lista vazia')

    return max(lst), min(lst), # O(n + n) = O(2n) = O(n)


def max_min2(lst):
    """
    Calculate the maximum and minimum of a list lst (lista nao ordenada)
    :param: lst: list
    :return: tuple: (max, min)
    """
    if len(lst) == 0:
        raise Exception('Lista vazia')

    max_value = min_value = lst[0]

    for value in lst:
        if value > max_value:
            max_value = value
        elif value < min_value:
            min_value = value

    return  max_value, min_value # O(n)


def max_min3(lst):
    """
    Calculate the maximum and minimum of a list lst (lista nao ordenada)
    :param: lst: list
    :return: tuple: (max, min)
    """
    if len(lst) == 0:
        raise Exception('Lista vazia')

    max_value = min_value = lst.pop() # O(1) - ultimo elemento

    for value in lst:
        if value > max_value:
            max_value = value
        elif value < min_value:
            min_value = value

    return  max_value, min_value # O(n)


if __name__ == '__main__':

    lista_random = list(range(-99,100)) 
    shuffle(lista_random)
    print(max_min(lista_random))

    print(max_min2(lista_random))

    print(max_min3(lista_random))

    test =( [4], [1,2], list(range(1,100)), [] )
    for l in test:
        print(max_min_ord(l))

