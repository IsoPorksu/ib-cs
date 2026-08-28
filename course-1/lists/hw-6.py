from random import *
n = 10
list_of_lists = [sample(list(range(n)), n) for _ in range(5)]
flat_list = []
for lst in list_of_lists:
    for element in lst: flat_list.append(element)
print(list_of_lists)
print(flat_list)