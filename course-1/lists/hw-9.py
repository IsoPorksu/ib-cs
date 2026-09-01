def transpose(list):
    return [[list[j][i] for j in range(len(list))] for i in range(len(list[0]))]
print(transpose([[1, 2, 3], [4, 5, 6]]))