def read_words_from_url():
    import requests
    response = requests.get("https://raw.githubusercontent.com/dwyl/english-words/refs/heads/master/words_alpha.txt", stream=True)
    words = [line.decode("utf-8").strip() for line in response.iter_lines()]

    return words

print(read_words_from_url()[-10:])

def seq_search(key, array):
    index = 0
    while index<len(array):
        if index == key: return array[index]
        index += 1
    return False

def bin_search(key, array):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if mid == key: return array[mid]
        if mid < key: left = mid + 1
        else: right = mid - 1
    return -1

print(seq_search(129209, read_words_from_url()))
print(bin_search(129209, read_words_from_url()))