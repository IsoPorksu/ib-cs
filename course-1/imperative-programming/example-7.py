s = int(input("Enter a positive integer s: "))

valid = False
n = 1
while not valid:
    if (n * (n + 1)) / 2 > s:
        valid = True
    else: n += 1
print("The smallest integer n such that n(n+1)/2 > s is:", n)