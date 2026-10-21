def seq_search(key, array):
    index = 0
    while index<len(array):
        if array[index] == key: return True
        index += 1
    return False

arr = [7, -22, 4, 56, 8]
print(seq_search(4, arr))
print(seq_search(57, arr))
