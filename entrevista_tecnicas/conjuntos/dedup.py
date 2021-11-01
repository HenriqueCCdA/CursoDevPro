def dedup(lst):
    '''Remove duplicates from lst
    
    :param lst: a list
    :return: new list without duplicated elements

    linear for time and space
    '''
    result = []
    repeared = set()
    for ele in lst:
        if ele not in repeared:
            result.append(ele)
            repeared.add(ele)
    return result

print(dedup(['banana', 'banana', 'banana', 'abacaxi', 'caqui']))