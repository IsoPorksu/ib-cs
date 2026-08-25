a = int(input("Please enter a positive integer a: "))
b = int(input("Please enter a positive integer b: "))
i = 1
while True:
    if i % a == 0 and i % b == 0: break
    else: i += 1
print(i)