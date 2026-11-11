def seq_search(key, array):
    index = 0
    while index<len(array):
        if index == key: return array[index]
        index += 1
    return False