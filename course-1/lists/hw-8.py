words = []
while (word := input("Please enter a word: ")) != "!":
    words.append(word)
indices = []; words_new = []
print("Second stage")
while (index := int(input("Please enter an index: "))) >= 0: indices.append(index)
for i in range(len(words)):
    if i not in indices:
        words_new.append(words[i])
print("The original list of words is:", words)
print("The list of indices is:", indices)
print("The new list of words is:", words_new)