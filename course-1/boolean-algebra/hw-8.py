def test_prime(number):
    i = 2
    while i < number:
        if number % i == 0: return False
        i += 1
    return True
for j in range (1, 100):
    if test_prime(j): print(str(j), end=" ")
print()
k = 1
count = 0
while count < 100:
    if test_prime(k): print(str(k), end=" "); count += 1
    k += 1