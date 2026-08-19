smallest = 0
largest = 0

for n in range (0, 51):
    eval = n * (n - 30) * (n - 50)
    if eval < smallest: smallest = eval
    if eval > largest: largest = eval

print('Smallest value:', smallest)
print('Largest value:', largest)