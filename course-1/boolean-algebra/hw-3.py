s = int(input("Please enter a positive integer s: "))
n = 1
while True:
    if ((n**3) - (10*(n**2))) > s: break
    else: n += 1
print(f"n = {n}, n^3 - 10n^2 = {(n**3) - (10*(n**2))}")