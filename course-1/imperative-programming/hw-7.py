n = int(input("Please enter a positive integer n: "))

smallest = False
while not smallest:
    if ((n^3 - 16) % 47) == 0:
        smallest = True
    else:
        n += 1
print("The smallest integer n such that n^3 - 16 is divisible by 47 is:", n)