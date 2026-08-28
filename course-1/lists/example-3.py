lst = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "ugli fruit", "watermelon", "xigua", "yellow passion fruit", "zucchini"]
for item in lst:
    if len(item) < 5: lst.remove(item)
print(lst)