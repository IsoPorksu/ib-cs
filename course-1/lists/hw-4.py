word = ""
lst = []
while word != "!":
    word = input("Please enter a word: ")
    lst.append(word)
word = ""
print("Second stage")
while word != "!":
    word = input("Please enter a word: ")
    if word in lst and word != "!": print("hit")