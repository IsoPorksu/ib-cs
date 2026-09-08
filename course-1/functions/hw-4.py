def share(a, b):
    response = False
    for _, element in enumerate(a):
        for i in range(0, len(b)):
            if element == b[i]:
                response = True
    return response

a = [1, 2, 3]
b = [4, 5, 6]
print(share(a, b))

a = [1, 2, 3]
b = [4, 5, 3]
print(share(a, b))