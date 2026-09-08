def swap(lst, ind1, ind2):
    temp = lst[ind1]
    lst[ind1] = lst[ind2]
    lst[ind2] = temp
    return lst