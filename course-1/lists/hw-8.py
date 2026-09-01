words = []
while (word := input("Please enter a word: ")) != "!":
    words.append(word)
indices = []; words_new = words.copy()
print("Second stage")
while (index := int(input("Please enter an index: "))) >= 0:
    if 0 <= index < len(words):
        indices.append(index)
        words_new.remove(words[index])
print("The original list of words is:", words)
print("The list of indices is:", indices)
print("The new list of words is:", words_new)