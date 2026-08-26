x = int(input("Please enter integer x: "))
y = int(input("Please enter integer y: "))
result = 1
while y > 0:
    if y % 2 == 0:
        y /= 2
        x = x * x
    else:
        y -= 1
        result *= x
print(result)