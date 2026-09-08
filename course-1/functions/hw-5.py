def remove(orig, x, out):
    out = orig.copy()
    removed_counter = 0
    for _, element in enumerate(orig):
        if element == x:
            out.remove(x)
            removed_counter += 1
    for i in range(removed_counter+1): out.append(0)
    return out

orig = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
x = 4
out = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6]

print(remove(orig, x, out))