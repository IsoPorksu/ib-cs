def read_words_from_url():
    import requests
    response = requests.get("https://raw.githubusercontent.com/dwyl/english-words/refs/heads/master/words_alpha.txt", stream=True)
    words = [line.decode("utf-8").strip() for line in response.iter_lines()]
    words.sort()

    return words

print(read_words_from_url()[-10:])

def seq_search(key, array):
    index = 0
    while index<len(array):
        if array[index] == key: return index
        index += 1
    return False

def bin_search(key, array):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == key: return mid
        if array[mid] < key:
            print(mid, key, array[mid])
            left = mid + 1
        else: right = mid - 1
    return False

print(seq_search("granola", read_words_from_url()))
print(bin_search("granola", read_words_from_url()))