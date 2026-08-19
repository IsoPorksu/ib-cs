i = 9
while i < 66:
    print(f'{i} ', end='')
    i += 4
print()
j = 3
for i in range (1, 14):
    print(f'{j} ', end='')
    j = j*2
print()
k = 1
for i in range (1, 41):
    if i % 4 == 0: print('-1 ', end='')
    else: print(f'{k} ', end='')
    k += 1