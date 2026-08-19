w = int(input("Enter the weight of your package as an integer (in kg): "))

if w <= 2:
    p = 3
elif w <= 5:
    p = 3 + (2 * (w - 2))
else:
    p = 9 + (3 * (w - 5))

print("The cost of shipping your package is:", p)