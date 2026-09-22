def uniques(numbers):
    for i, n in enumerate(numbers):
        if numbers.index(n) != i: return False
    return True

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(uniques(numbers))

numbers = [0, 1, 2, 3, 5, 5, 6, 7, 8, 9]
print(uniques(numbers))