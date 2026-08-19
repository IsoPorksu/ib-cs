"""# Part 1
a = int(input("Enter integer a: "))
b = int(input("Enter integer b: "))

if a >= 100:
    if b >= 50: print(1)
    else: print(0)
else: print (0)"""

# Part 2
a = int(input("Enter integer a: "))
b = int(input("Enter integer b: "))

if a >= 100:
    if b >= 50: print(1)
    else: print(0)
elif b >= 100:
    if a >= 50: print(1)
    else: print(0)
else: print(0)