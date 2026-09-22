n = 6

for i in range(n):
    for k in range(n):
        if k-1<i: print("*", end="")
        else: print("-", end="")
    print()

print()

for i in range(n, 0, -1):
    for k in range(n):
        if k<i:
            if k % 2 == 0: print("*", end="")
            else: print("-", end="")
    print()