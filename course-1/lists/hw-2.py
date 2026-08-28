integer = 1
positive = []
negative = []
while integer != 0:
    integer = int(input("Please enter integers: "))
    if integer > 0: positive.append(integer)
    if integer < 0: negative.append(integer)
print(positive, negative)