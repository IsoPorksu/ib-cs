n = 7
for k in range (n, 0, -1):
    for num in range (1, k+1):
        print(num, end="")
    k -= 1
    print()