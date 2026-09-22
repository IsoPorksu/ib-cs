def sym_diff(a, b):
    lst = []
    for element in a:
        if element not in b: lst.append(element)
    for element in b:
        if element not in a: lst.append(element)
    return lst

a = [4, 4, 6, 11, -2, 3]
b = [5, 11, 11, -3, 3, 5]
print(sym_diff(a, b))