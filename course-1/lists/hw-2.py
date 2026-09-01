positive = []; negative = []
while (integer := int(input("Please enter integers: "))) != 0:
    if integer > 0: positive.append(integer)
    if integer < 0: negative.append(integer)
print(positive, negative)