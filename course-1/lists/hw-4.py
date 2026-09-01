lst = []
while (word := input("Please enter a word: ")) != "!": lst.append(word)
print("Second stage")
while (word := input("Please enter a word: ")) != "!":
    if word in lst: print("hit")