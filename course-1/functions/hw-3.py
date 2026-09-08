def read_ints():
    lst = []
    while (word := input("Please enter a word: ")):
        lst.append(word)
    return lst