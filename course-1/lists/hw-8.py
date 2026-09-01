word = ""
words = []
while word != "!":
    word = input("Please enter a word: ")
    words.append(word)
words.remove("!")
index = 0
indices = []; words_new = words.copy()
print("Second stage")
while index >= 0:
    index = int(input("Please enter an index: "))
    if 0 <= index < len(words)+1:
        indices.append(index)
        words_new.remove(words[index])
print("The original list of words is:", words)
print("The list of indices is:", indices)
print("The new list of words is:", words_new)