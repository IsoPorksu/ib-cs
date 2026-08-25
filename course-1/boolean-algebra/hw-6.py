number = int(input("Please enter a number to check: "))
i = 2
while i < number:
    if number % i == 0: print(str(number) + " is not a prime number."); exit()
    i += 1
print(str(number) + " is a prime number.")