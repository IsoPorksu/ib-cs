def test_perfect(n):
    sum_divisors = 0
    for i in range(1, n):
        if n % i == 0: sum_divisors += i
    return sum_divisors == n
for n in range(1, 10000):
    if test_perfect(n): print(str(n), end=" ")